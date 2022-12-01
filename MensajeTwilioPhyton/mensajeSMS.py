from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC86447003833414acee2cc336ffcb6b94"

# Your Auth Token from twilio.com/console
auth_token  = "68a92b58b974ff568146115815c3871b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+573015145503", 
    from_="+16672290538",
    body="Haaa funcionado!!")

print(message.sid)


