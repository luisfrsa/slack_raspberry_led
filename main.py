import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from customer_actions import CustomerActions
from dotenv import load_dotenv
# from led import LedStrip
# from colors import Colors

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
APP_TOKEN = os.getenv('APP_TOKEN')

app = App(token=BOT_TOKEN)

# for customerActions in CustomerActions:
#      print(customerActions)

# Initializes your app with your bot token and socket mode handler
app = App(token=BOT_TOKEN)


# ledStrip = LedStrip()
# colors = Colors(ledStrip)


# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    # say(f"ASD there <@{message['user']}>!")
    for key, value in message.items():
        print(key, ' : ', value)
    print("message_hello!")
    text = message['text']
    print("the msg was",text)
    print(text)
    # say("The text is: " + text)
    # colors.writeAll(colors.ORANGE)
    # colors.off()
    # colors.writeAll(colors.ORANGE)
    # colors.off()

@app.event("message")
def handle_message_events(body, logger):
    print("handle_message_events!")
    logger.info(body)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, APP_TOKEN).start()