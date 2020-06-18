def config():
	
	return dict()
def mail():
	from gluon.tools import Mail
	mail = Mail()
	mail.settings.server = 'smtp.gmail.com'
	mail.settings.sender = ''
	
	mail.settings.login = 'juanulivar@gmail.com:trulalero452569' 
	mail.send('archy_22_2@hotmail.com',
	  'Probando',
	  'Tierra llamando a guille XD')

	return dict()	
def sms():
	from gluon.contrib.sms_utils import SMSCODES, sms_email
	email = sms_email('1 (111) 111-1111','T-Mobile USA (tmail)')
	mail.send(to=email, subject='prueba', message='prueba')

	return dict()