
from configs.utils import Singleton


class strings(object):
	__metaclass__ = Singleton
	
	salutation = "Boss"
	me	=	"Jarvis Poi"


	connecting_string	=	"Connecting to %s : %s"
	first_welcome_msg = "Hey %s, This is "+me+". I act as your personal assistant. Let me know how i can help you."
	bot_start	=	salutation+", "+me+" powered up!"
	cannot_connect	=	"Sorry "+salutation+"! Cannot connect to %s. can you please check internt connection?!"
	not_secure_connection	=	""+salutation+", Waring: Connection is not secure!"
	wrong_password = "Looks like wrong password for account "+salutation
	no_sasl = "Warning: unable to perform SASL auth os %s. Old authentication method used!"
	status = "Hey "+salutation+", welcome.. how can i help you?"
	changed_status_to = "Changed status to \"%s\" sucessfully "+salutation+"!"
	not_permitted = "You dont have permission to do this :-/ contact admin!!"
	didnt_understand = "Sorry "+salutation+". I dint understand what you meant! Please consider upgrading me :("
