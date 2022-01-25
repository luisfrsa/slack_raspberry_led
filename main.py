from customer_actions import CustomerActions
from led import LedStrip
from write_led import WriteLed
from slack import SlackBot
import time


led_strip = LedStrip()
write_led = WriteLed(led_strip)

slack_bot = SlackBot(write_led)
app = slack_bot.app

myDict = {}

myDict["user"] = "U0251J73N0Z" #user

# print("user")
# slack_bot.parseAction(myDict)
# time.sleep(3)

# myDict["bot_id"] = "B017B9Y5A75" # new subs
# print("new subs")
# slack_bot.parseAction(myDict)
# time.sleep(3)


# myDict["bot_id"] = "B016WBNJ7P1" # expans
# print("expans")
# slack_bot.parseAction(myDict)
# time.sleep(3)

# myDict["bot_id"] = "B017PNTEQE5" # addon
# print("addon")
# slack_bot.parseAction(myDict)
# time.sleep(3)

# myDict["bot_id"] = "B017H9MT02G" # upgrade
# print("upgrade")
# slack_bot.parseAction(myDict)
# time.sleep(3)


# write_led.gradient(write_led.BLUE,5)
# write_led.off()

# write_led.gradient2(write_led.RED, write_led.GREEN,2)
# write_led.off()

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    # say(f"ASD there <@{message['user']}>!")
    # for key, value in message.items():
    #     print(key, ' : ', value)
    # text = message['text']
    # user = message['user']
    # say("The text is: " + text)
    # write_led.writeAll(write_led.BLUE)
    # write_led.off()
    # write_led.writeAll(write_led.ORANGE)
    # write_led.off()
    slack_bot.parseAction(message)

# Start your app
if __name__ == "__main__":
    slack_bot.socker_mode.start()