from customer_actions import CustomerActions
from led import LedStrip
from write_led import WriteLed
from slack import SlackBot
import time


led_strip = LedStrip()
write_led = WriteLed(led_strip)

slack_bot = SlackBot(write_led)
app = slack_bot.app

# for tests see ./test.txt

myDict = {}
myDict["bot_id"] = "B017B9Y5A75"  # new subs
print("new subs")
slack_bot.parseAction(myDict)
time.sleep(3)


myDict["bot_id"] = "B016WBNJ7P1"  # expans
print("expans")
slack_bot.parseAction(myDict)
time.sleep(3)


# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("")
def message_hello(message, say):
    slack_bot.parseAction(message)


# Start your app
if __name__ == "__main__":
    slack_bot.socker_mode.start()
