import os
import slack
from datetime import datetime

def getCurrentTime():
    output_string= '';
    now = datetime.now()
    hour = now.hour
    minute = now.minute

    if (hour > 12):
        adjusted_hour = hour - 12
        formatted_time = str(adjusted_hour) + ':' + str(minute) + ' PM'
        output_string = 'Sign Out ' + formatted_time
    else:
        formatted_time = str(hour) + ':' + str(minute) + ' AM'
        output_string = 'Sign In ' + formatted_time

    return output_string

slack_token = os.environ["SLACK_API_TOKEN"]
client = slack.WebClient(token=slack_token)

client.chat_postMessage(
    channel='CHANNEL_ID',
    text= getCurrentTime()
)
