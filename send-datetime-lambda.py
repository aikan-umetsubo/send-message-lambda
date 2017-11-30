import datetime
import requests
import os
import json

slack_aws_url = os.environ['SLACK_URL']

def lambda_handler(event, context):
    requests.post(slack_aws_url, data = json.dumps({
        'text': u'now is ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'username': u'aws lambda',
        'icon_emoji': u':joy:'
    }))

