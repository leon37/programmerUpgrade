from twilio.rest import Client

accountSID = 'ACbfc8f421b841f05e93397840e462b2ee'
authToken = 'eeed012c310c63fae37807cd578893fd'

twilioCli = Client(accountSID, authToken)

myTwilioNumber = '+16506402874'
myCellPhone = '+8618200143014'

message = twilioCli.messages.create(
    to = myCellPhone,
    from_ = myTwilioNumber,
    body = 'Hello from python!'
)

print(message.sid)
