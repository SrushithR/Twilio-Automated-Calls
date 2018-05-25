# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC5*******************811d8e4d445a"
auth_token = "ef65********************aeb3"
client = Client(account_sid, auth_token)

call = client.calls.create(
    # the verified number to which you wanna call
    to="+918686519259",
    # the number that you just purchased on Twilio
    from_="+18034087781",
    # the invoke URL from API Gateway
    url="https://lskcr****.execute-api.us-east-1.amazonaws.com/dev/twilio"
)
# An SID is generated for every call. It is useful for debugging
print(call.sid)