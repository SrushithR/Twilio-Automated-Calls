"""
    Function to return TwilML content back to the client
"""

def lambda_handler(event, context):
    print 'input to lambda {}'.format(event)
    xml_content = """<?xml version="1.0" encoding="utf-8"?><Response><Say voice = "alice">Hi! Hope you are having a great time hacking code in the meetup</Say></Response>"""
    return {'body' : xml_content}