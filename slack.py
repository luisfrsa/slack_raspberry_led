import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from customer_actions import CustomerActions


class SlackBot:
    def __init__(self, write_led):
        load_dotenv()
        BOT_TOKEN = os.getenv('BOT_TOKEN')
        APP_TOKEN = os.getenv('APP_TOKEN')
        self.app = App(token=BOT_TOKEN)
        self.socker_mode = SocketModeHandler(self.app, APP_TOKEN)
        self.write_led = write_led

    
    def parseAction(self,message):
        # message['bot_id'] = CustomerActions.ADDON_PURCHASE
        bot_id = message['user']
        if(bot_id == CustomerActions.ADDON_PURCHASE):
            print("CustomerActions.ADDON_PURCHASE")
            self.addon_purchase()
            return
        if(bot_id == CustomerActions.EXPANSION):
            print("CustomerActions.EXPANSION")
            self.expansion()
            return
        if(bot_id == CustomerActions.NEW_SUBSCRIPTION):
            print("CustomerActions.NEW_SUBSCRIPTION")
            self.new_subscription()
            return
        if(bot_id == CustomerActions.UPGRADE):
            print("CustomerActions.UPGRADE")
            self.upgrade()
            return
        
        print ("Other")
        print ("Test")
        print(CustomerActions.TEST)
        print ("MsgUSer")
        print(message['user'])
        print(message)
        if(message['user'] == CustomerActions.TEST):
            self.test()


    
    def addon_purchase(self):
        write_led.writeAll(write_led.RED)
        write_led.off()
    
    def expansion(self):
        write_led.writeAll(write_led.GREEN)
        write_led.off()
    
    def new_subscription(self):
        write_led.writeAll(write_led.BLUE)
        write_led.off()
    
    def upgrade(self):
        write_led.writeAll(write_led.ORANGE)
        write_led.off()
    
    def test(self):
        write_led.writeAll(write_led.YELLOW)
        write_led.off()
        

