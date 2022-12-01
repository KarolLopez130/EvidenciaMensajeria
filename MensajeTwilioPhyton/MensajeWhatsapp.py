from twilio.rest import Client 
 
account_sid = 'AC86447003833414acee2cc336ffcb6b94' 
auth_token = '68a92b58b974ff568146115815c3871b' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
    from_='whatsapp:+14155238886',  
    body='sopasssssSS',      
    to='whatsapp:+573015145503' 
) 
 
print(message.sid)