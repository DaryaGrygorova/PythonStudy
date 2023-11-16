import json
import threading
import requests

REDDIT_USERNAME = 'WalterSmith7763'
REDDIT_PASSWORD = '7Ux5M!7ugPTF3HL'

def drink_coffee():
    pass

def reddit():  # застарілий код (не працює)
    # create dict with username and password
    user_pass_dict = {'user': REDDIT_USERNAME,
                  'passwd': REDDIT_PASSWORD,
                  'api_type': 'json' }

    # set the header for all the following requests
    headers = {'user-agent': '/u/TankorSmash\'s API python tutorial bot', }

    # create a requests.session that'll handle our cookies for us
    client = requests.session()
    client.headers = headers

    # make a login request, passing in the user and pass as data
    r = client.post(r'http://www.reddit.com/api/login', data=user_pass_dict)

    # optional print to confirm error-free response
    # pprint(r.content)

    # turns the response's JSON to a native python dict
    j = json.loads(r.content)

    # grabs the modhash from the response
    client.modhash = j['json']['data']['modhash']

    # prints the users modhash
    print(
    '{user_pass_dict}\'s modhash is: {mh}'.format(user_pass_dict['name'], mh=client.modhash))
