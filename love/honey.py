from twilio.rest import Client

account_sid = 'AC4e2404abee6190c795102478f301cf45'
auth_token = 'fca914443b0574be1acc703676c4e572'
client = Client(account_sid, auth_token)

def send_love():
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='Hi!, Good Morening😀😀\n From: Ashraf',
                                  to='whatsapp:+919140487652'
                              )

    print(message.sid)
