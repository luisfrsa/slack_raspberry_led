import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from customer_actions import CustomerActions
from dotenv import load_dotenv
from led import LedStrip
from write_led import WriteLed

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
APP_TOKEN = os.getenv('APP_TOKEN')

app = App(token=BOT_TOKEN)

# for customerActions in CustomerActions:
#      print(customerActions)

# Initializes your app with your bot token and socket mode handler
app = App(token=BOT_TOKEN)


ledStrip = LedStrip()
write_led = WriteLed(ledStrip)

write_led.gradient2(write_led.RED, write_led.GREEN)
write_led.off()

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    # say(f"ASD there <@{message['user']}>!")
    # for key, value in message.items():
        # print(key, ' : ', value)
    text = message['text']
    say("The text is: " + text)
    write_led.writeAll(write_led.ORANGE)
    write_led.off()
    write_led.writeAll(write_led.ORANGE)
    write_led.off()

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, APP_TOKEN).start()