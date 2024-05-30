from twilio.rest import client # This uses twilio api to make sms transferable

account_sid = 'random_key'
auth_token = '[AuthToken]'
client = client(account_sid, auth_token)


message = client.messages.create(
    from_ = 'twilio generated num',
    to = 'receiver num'
)

print(message.sid)