import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from customer_actions import CustomerActions
from dotenv import load_dotenv

load_dotenv()

# for customerActions in CustomerActions:
#      print(customerActions)

BOT_TOKEN = os.getenv('BOT_TOKEN')
APP_TOKEN = os.getenv('APP_TOKEN')

# Initializes your app with your bot token and socket mode handler
app = App(token=BOT_TOKEN)


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

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, APP_TOKEN).start()