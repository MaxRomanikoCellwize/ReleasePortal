from slackclient import SlackClient
import os

#slack_token = os.environ[]
sc = SlackClient("xoxp-20663887266-154587478434-301656359095-9a3169f45ca985763bcb1018a2c36728")

sc.api_call(
  "chat.postMessage",
  channel="#release-portal",
  text="Mr. Roy Bachar, I'm texting you from the realese portal BOT, what do you have to say???"
)