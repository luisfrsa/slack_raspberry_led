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
        # message.get('bot_id') = CustomerActions.ADDON_PURCHASE.value
        bot_id = message.get('bot_id')
        print("bot_id")
        print(bot_id)

        if(bot_id == CustomerActions.ADDON_PURCHASE.value):
            print("CustomerActions.ADDON_PURCHASE")
            self.addon_purchase()
            return
        if(bot_id == CustomerActions.EXPANSION.value):
            print("CustomerActions.EXPANSION")
            self.expansion()
            return
        if(bot_id == CustomerActions.NEW_SUBSCRIPTION.value):
            print("CustomerActions.NEW_SUBSCRIPTION")
            self.new_subscription()
            return
        if(bot_id == CustomerActions.UPGRADE.value):
            print("CustomerActions.UPGRADE")
            self.upgrade()
            return
        
        print ("Other")
        print ("Test")
        print(CustomerActions.TEST.value)
        print ("MsgUSer")
        print(message.get('user'))
        print(message)
        if(message.get('user') == CustomerActions.TEST.value):
            self.test()

    def test(self):
        self.blink()
 
    def new_subscription(self):
        self.blink()

    def expansion(self):
        self.blink()
    
    def addon_purchase(self):
        self.spiranAndBlink()
    
    def upgrade(self):
        self.spiranAndBlink()

    def blink(self):
        for x in range(0,3):
            self.write_led.writeAll(self.write_led.SEVEN_SHIFTS_MINT,1)
            self.write_led.off()
    
    def spiranAndBlink(self):
        for x in range(0,2):
            self.write_led.lineProgress(self.write_led.SEVEN_SHIFTS_ORANGE,2)
            self.write_led.off()
            for x in range(0,3):
                self.write_led.writeAll(self.write_led.SEVEN_SHIFTS_ORANGE,1)
                self.write_led.off()
            

        
        

