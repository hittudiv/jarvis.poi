import inspect
from configs.utils import Singleton
from configs.config import configs
import os
import glob
# from plugins.commander_regex import commander_regex
from plugins import *
import plugins


class presence:
	conn	=	None
	def __init__(self):
		pass
	def handle(self, conn, presence):
		print "-"*10
		print presence.getFrom(), ",", presence.getFrom().getResource(), ",", presence.getType(), ",", presence.getStatus(), ",", presence.getShow()
		print "~"*10



class im:
	def __init__(self):
		pass

	def handle(self, conn, text, user):
		return command().handle(conn, text, user);

class command:
	__metaclass__ = Singleton

	show = "available"
	status = "PyGtalkRobot"

	def __init__(self):
		pass

		#print self.commands
	def handle(self, conn, text, user):
		plugins_list=[ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/plugins/commander_*.py")]
		# print (plugins)
		for i in plugins_list:
			try:
				class_name = getattr(plugins, i, i)
				if(configs().prod==0):
					reload(class_name)
				reply, status, availability	=	class_name.commander().try_text(text, user)
				return reply, status, availability
			except:
				pass
		return None
		# commander_regex().try_text(text, user)
		


