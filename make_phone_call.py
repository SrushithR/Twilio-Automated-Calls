# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC5ed8a0e4dfb2e39869e6b11d8e4d445a"
auth_token = "ef651e0abc62c191220ff93d214caeb3"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+918686519259",
    from_="+18034087781",
    url="https://lskcrt3x37.execute-api.us-east-1.amazonaws.com/dev/twilio"
)

print(call.sid)
