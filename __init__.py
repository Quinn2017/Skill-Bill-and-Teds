import pygsheets

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler

gc = pygsheets.authorize(outh_file='client_id.json', outh_nonlocal=True)
sh = gc.open('tonyquinn2018')
wks = sh.sheet1
wks.update_cell('A1','test')
sh.share("charlesldumais@gmail.com")

class InventorySkill(MycroftSkill):
    def __init__(self):
        super(InventorySkill, self).__init__(name="InventorySkill")

    def speak_inventory(self, update_cell):
        self.speak()

    @intent_handler(IntentBuilder("InventoryIntent").require("InventoryKeyword"))
    def handle_Inventory_intent(self, message):
        self.speak("Yes, I have your Google Spreadsheet right here.", expect_response=True)

def create_skill():
    return InventorySkill()