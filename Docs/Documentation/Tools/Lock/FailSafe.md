#initialize

```
import MTM_UTILITIES
toolObj		= MTM_UTILITIES.Facts.getTools().getLock().getFailSafe();
```
## Desc

Global locks by name that will delete themselves if the tread that took them dies, if the expiration is reached or if the originator releases the thread.

## Methods:

### set:

Take a lock.

```
name			= "myGlobalLockName"; ## unique name for your lock
wait			= 1;## how long are you willing to wait for the lock if it already exists. default: 1s
expire			= 15; ## how long before the lock automatically terminates. default: 15s
threadEvent	= toolObj.set(name, wait, expire); ##set when lock is released

```

### unset:

Release a lock.

```
name			= "myGlobalLockName"; ## unique name for your lock
throw			= True;## throw if we do not own the lock. default: True
toolObj			= toolObj.unset(name, throw); ##self

```
