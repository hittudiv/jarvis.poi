

from configs.utils import Singleton

class configs(object):
	__metaclass__ = Singleton


	#all variables here
	prod=1
	# debug		=	['nodebuilder', 'dispatcher', 'gen_auth', 'SASL_auth', 'bind', 'socket', 'CONNECTproxy', 'TLS', 'roster', 'browser', 'ibb']
	debug		=	[]
	settings = {}
	prod_settings = {
		"server" 			:	"talk.google.com",
		"port"				:	443,
		"BOT_GTALK_USER" 	: 	'jarvis.poi@gmail.com',
		"BOT_GTALK_PASS" 	: 	'cheater1143',
		"BOT_ADMIN" 		: 	['hittudiv@gmail.com'],
	}
	dev_settings =	{
		"server" 			:	"hittudiv.com",
		"port"				:	5222,
		"BOT_GTALK_USER" 	: 	'jarvis.poi@hittudiv.com',
		"BOT_GTALK_PASS" 	: 	'cheater1143',
		"BOT_ADMIN" 		: 	['hittudiv@hittudiv.com'],
	}




	#All logic here. for switching variables
	if(prod==0):
		settings=dev_settings
	else:
		settings=prod_settings