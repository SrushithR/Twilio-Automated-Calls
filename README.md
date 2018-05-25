# twilio_automated_calls
Python code to make automated calls using Twilio Programmable Voice service and AWS services like AWS Lambda and API Gateway

Prerequisites:

Make sure the following software/modules are installed:  
	1. Python 2.7 (because we are going to write the core logic in Python)
	2. Twilio modules (Twilio is for making automated calls) 
	
Step 1: Sign up on Twilio

Twilio is a cloud communications platform as a service company and offers an array of services. We will be using the Twilio programmable voice service. 
Sign up for free on Twilio at https://www.twilio.com/try-twilio.

Step 2: Purchase a voice enabled Twilio phone number 

You need to purchase a Twilio phone number. Once you have are signed-in, navigate to Programmable Voice and under the Numbers section, choose "buy a number" in the console.

			


Select your preferred country and "Voice" under the capabilities section and search. Twilio gives a list of available numbers - chose the one you like (you may have observed that each number costs $1 per month). Congo! Now you have a number to play with. 

Step 3: Create an AWS Lambda function

Sign In/Sign Up to your AWS account and navigate to Lambda (https://console.aws.amazon.com/lambda/home). Create a new function with Python 2.7 as the runtime.


 

Paste the following code into the online editor and save it:

def lambda_handler(event, context):
    # TODO implement
    xml_content = """<?xml version="1.0" encoding="utf-8"?><Response><Say voice = "alice">Hi! Hope you are having a great time hacking code in the meetup</Say></Response>"""
    return {'body' : xml_content}



Step 4: Create an API and resource on API Gateway

Navigate to API Gateway (https://console.aws.amazon.com/apigateway/home) in the services section and create an API as shown below:



Under the 'Actions' button, select 'Create Resource' and fill the details as shown and create a resource:



Step 5: Create a method

Create a POST method under the created resource and input to the just created labmda function (twilio) under the 'Lambda Function' tab






Once saved, the Method Execution page would like this:


Add 'application/x-www-form-urlencoded' as the mapping template under the 'Body Mapping Templates' of the 'Integration Response' (click on use current settings when a message is prompted) and define the value as:

{
        "reqbody":"$input.path('$')"
}



Save and navigate back to the 'Method Execution'

Click the 'Integration Response' and edit the 'application/json' Content-Type to 'application/json' with a template as follows and save it:

#set($inputRoot = $input.path('$'))
$inputRoot.body



Hit the 'Test' button in the Method Execution page and test the method. The response would be:



Step 6: Deploy the API

After a successful test, its time to deploy the API. Select the POST method and click on 'Deploy API' under the Actions tab




Add the following details in the deployment pop-up and deploy:

				

Once deployed, navigate to your method under the 'dev' section and copy the 'Invoke URL'

			

Step 3: Make an outbound call

Before you can make an outbound call, you need the Twilio credentials for authorization in our python code. They can be found at the Twilio console dashboard (https://www.twilio.com/console), note down the account SID and the Auth token.

Here is the python code to make an outgoing call, let's save it as make_phone_call.py:

from twilio.rest import Client

# Replace the account_sid and auto_token with your credentials
account_sid = "A****************************a"
auth_token = "e****************************3"
client = Client(account_sid, auth_token)

# to and from numbers should include the country code
call = client.calls.create(
    to="+919********1",
    from_="+18********1",
    url="https://handler.twilio.com/twiml/EH5b806e705eb0c9********"
)

print call.sid
print 'call successfully made'

Before you run the above snippet, 

	• Replace the account_sid and auth_token with your credentials
	• to -  The number you want to call
	• from - The number you just bought. Since, we are still in the trial account (can be upgraded by adding credit/debit card information), you must verify the 'to' number under the 'Verified Caller IDs' (https://www.twilio.com/console/phone-numbers/verified). Give your number for testing purposes
	• URL - A URL that returns TwiML (Twilio Markup Language) with instructions on what should happen when the user picks up the call. In our case it is the 'Invoke URL' from the previous step

Once all the details are updated in the code, run it!

python make_phone_call.py


