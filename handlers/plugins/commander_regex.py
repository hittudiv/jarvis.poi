from configs.utils import Singleton
from configs.config import configs
import inspect
import re
from configs.strings import strings
import subprocess
import time

class commander:

	__metaclass__ = Singleton

	conn = None
	commands = None
	command_prefix = 'command_'
	GO_TO_NEXT_COMMAND = 'go_to_next'
	BOT_ADMIN = configs().settings["BOT_ADMIN"]

	def initCommands(self):
		if self.commands:
			self.commands.clear()
		else:
			self.commands = list()
		for (name, value) in inspect.getmembers(self):
			if inspect.ismethod(value) and name.startswith(self.command_prefix):
				self.commands.append((value.__doc__, value))


	def try_text(self, text , user):
		if(not self.commands):
			self.initCommands()
		# print self.commands
		for (pattern, bounded_method) in self.commands:
			print "Testing [%s] against regex [%s]\n" % (text, pattern)
			match_obj = re.match(pattern, text)
			if(match_obj):
				reply, status, availability = bounded_method( user, text, match_obj.groups())
				return reply, status, availability
		return None



	def command_001_setState(self, user, message, args):
		'''(available|online|busy|dnd|away|idle|out|xa)( +(.*))?$(?i)'''
		show = args[0]
		status = args[1]
		jid = user.getStripped()

		# Verify if the user is the Administrator of this bot
		if jid in self.BOT_ADMIN:
			#put a logger in place?
			print jid, " changed status to ---> ", status
			return strings().changed_status_to%status, status, show
		return strings().not_permitted,None,None 

	def command_003_shell(self, user, message, args):
		'''(shell|bash)( +(.*))?$(?i)'''
		jid = user.getStripped()
		if jid in self.BOT_ADMIN:
			cmd = args[1]
			p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = ""
			for line in p.stdout.readlines():
				output += line
				# print line,
			# retval = p.wait()
			
			return output +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()), None, None
		return strings().not_permitted,None,None 


	def command_100_default(self, user, message, args):
		'''.*?(?s)(?m)'''
		return  time.strftime("%Y-%m-%d %a %H:%M:%S", time.localtime()), None, None

	