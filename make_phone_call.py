# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC5ed8a0e4df********1d8e4d445a"
auth_token = "ef651e0abc6*************ff93d214caeb3"
client = Client(account_sid, auth_token)

call = client.calls.create(
    # the verified number to which you wanna call
    to="+919916994022",
    # the number that you just purchased on Twilio
    from_="+18123018775",
    # the invoke URL from API Gateway
    url="https://ls******7.execute-api.us-east-1.amazonaws.com/dev/twilio"
)
# An SID is generated for every call. It is useful for debugging
print(call.sid)