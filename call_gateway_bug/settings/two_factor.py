import os
import configparser
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'secrets.ini'))

LOGIN_URL = 'two_factor:login'
LOGIN_REDIRECT_URL = 'two_factor:profile'

TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'

TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'

TWILIO_ACCOUNT_SID = config.get('twilio', 'TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config.get('twilio', 'TWILIO_AUTH_TOKEN')

TWILIO_CALLER_ID = config.get('twilio', 'TWILIO_CALLER_ID')