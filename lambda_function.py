"""
    Function to return TwilML content back to the client
"""

def lambda_handler(event, context):
    # for debugging, first print event contents
    print 'input to lambda {}'.format(event)

    # twilio expects an XML content for generating the voice. This is written in something strange called TwiML
    # Ignore all the blah blah in the angular brackets and the actual voice message is "Hi! ....".
    # The voice is spoken by Alice - <Say voice = "alice">
    # The actual voice content is within the <Response> tags
    xml_content = """<?xml version="1.0" encoding="utf-8"?><Response><Say voice = "alice">Hi! Hope you are having a great time hacking code in the meetup</Say></Response>"""

    # frustratingly, lambda can not send XML content so we are wrapping it in the dummy JSON variable
    dummy = {'body' : xml_content} 
    return dummy