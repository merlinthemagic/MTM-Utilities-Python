from .termination import Termination
import re

class RouterOS(Termination):
	
	def __init__(self):
		
		super().__init__();
		
	def rosToSecs(self, ts):
		return round((self.rosToMicroSecs(ts) / 1_000_000));
		
	def rosToMiliSecs(self, ts):
		return round((self.rosToMicroSecs(ts) / 1_000));
		
	def rosToMicroSecs(self, ts):
		##sample inputs
		##00:00:24.010
		##00:00:12
		##14w1d14h37m39s
		##3d16:56:02
	
		weeks = days = hours = minutes = seconds = micro = 0;
	
		# Peel off leading weeks/days, e.g. "14w1d..." or "3d..."
		m							= re.match(r'(?:(\d+)w)?(?:(\d+)d)?(.*)', ts);
		weeks_str, days_str, rest	= m.groups();
		weeks						= int(weeks_str) if weeks_str else 0;
		days						= int(days_str) if days_str else 0;
	
		if not rest:
			# nothing left, e.g. ts was just "14w1d"
			pass;
		elif ':' in rest:
			# colon-separated: "16:56:02", "00:00:24.010", "00:00:12"
			parts					= rest.split(':');
			if len(parts) == 3:
				h_str, m_str, s_str		= parts;
			elif len(parts) == 2:
				h_str, (m_str, s_str)	= '0', parts;
			else:
				h_str, m_str, s_str		= '0', '0', parts[0];
	
			hours				= int(h_str);
			minutes				= int(m_str);
	
			if '.' in s_str:
				sec_str, micro_str		= s_str.split('.');
				seconds					= int(sec_str);
				micro					= int(micro_str.ljust(6, '0')[:6]);
			else:
				seconds					= int(s_str);
		else:
			# letter-suffixed: "14h37m39s"
			hm					= re.match(r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$', rest);
			h_str, m_str, s_str	= hm.groups();
			hours				= int(h_str) if h_str else 0;
			minutes				= int(m_str) if m_str else 0;
			seconds				= int(s_str) if s_str else 0;
	
		total_seconds		= weeks * 7 * 86400 + days * 86400 + hours * 3600 + minutes * 60 + seconds;
		return (total_seconds * 1_000_000 + micro);
		
		