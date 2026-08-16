import threading, time
from .zulu import Zulu

class Process(Zulu):

	def __init__(self):
		self._locks				= {};
		self._owners			= {};
		self._releaseEvents		= {};
		self._refCount			= {};	# name -> int, active users of this lock (waiting + holding)
		self._procLock			= threading.Lock();

	def set(self, name, waitTimeout=1, expireTimeout=10):
	
		lock			= self._getOrCreateLock(name);	# bumps refCount
		curThread		= threading.current_thread();
	
		acquired		= lock.acquire(timeout=waitTimeout);
		if not acquired:
			self._releaseLockRef(name);	# we're not using it anymore, drop our ref
			raise TimeoutError("Could not acquire failsafe lock '"+name+"' in time", 1111);
	
		releaseEvent	= threading.Event();
		with self._procLock:
			self._owners[name]			= curThread;
			self._releaseEvents[name]	= releaseEvent;
	
		watcher	= threading.Thread(
			target	= self._watchOwner,
			args	= (name, curThread, releaseEvent, expireTimeout),
			daemon	= True
		)
		watcher.start();
	
		##consider extending the Event class so we can stuff an exception into it. That will come in handy
		##so a caller can be notified they set too short of a expireTimeout and the lock became open while they executed
		return releaseEvent;
	
	def unset(self, name, throw=True):
	
		curThread	= threading.current_thread();
		with self._procLock:
			if name in self._locks:
				owner	= self._owners.get(name);
				if owner is not curThread:
					if throw:
						raise RuntimeError("You do not own lock: '"+name+"'", 1111);
					else:
						return None;
	
		self._deleteLock(name);
		return self;
	
	def _watchOwner(self, name, ownerThread, releaseEvent, expireTimeout):
	
		deadline		= time.monotonic() + expireTimeout;
		pollInterval	= 0.5;
	
		while True:
			remaining	= deadline - time.monotonic();
			if remaining <= 0:
				self._deleteLock(name);
				return;
			else:
				waitTime	= min(pollInterval, remaining);
	
			if releaseEvent.wait(timeout=waitTime):
				return;
	
			if not ownerThread.is_alive():
				self._deleteLock(name);
				return
	
	def _getOrCreateLock(self, name):
		with self._procLock:
			if name not in self._locks:
				self._locks[name]		= threading.Lock();
				self._refCount[name]	= 0;
			self._refCount[name]	+= 1;
			return self._locks[name];
	
	def _releaseLockRef(self, name):
		with self._procLock:
			if name in self._refCount:
				self._refCount[name]	-= 1;
				if self._refCount[name] <= 0 and not self._locks[name].locked():
					del self._locks[name];
					del self._refCount[name];
	
	def _deleteLock(self, name):
		with self._procLock:
			if name in self._owners:
				del self._owners[name];
			if name in self._releaseEvents:
				self._releaseEvents[name].set();
				del self._releaseEvents[name];
	
		lock	= self._locks.get(name);
		if lock is not None:
			try:
				lock.release();
			except RuntimeError:
				pass
	
		self._releaseLockRef(name);

				
				
	
