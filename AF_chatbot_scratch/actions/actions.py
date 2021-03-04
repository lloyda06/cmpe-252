# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
import random

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        output = "Hello World!"

        dispatcher.utter_message(text=output)

        return []

class ActionReportCurrentTime(Action):
    
    def name(self) -> Text:
        return "action_report_current_time"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        # print("Current Time =", current_time)
        output = "It's " + current_time
        
        dispatcher.utter_message(text=output)
        
        return []
        
class ActionCheckMail(Action):
    
    def name(self) -> Text:
        return "action_check_mail"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        hasMail = bool(random.getrandbits(1))
        # hasMail = False
        print("Checked mail: ", hasMail)
        
        
        return [SlotSet("has_mail", hasMail)]
        
class ActionResetAirport(Action):

    def name(self) -> Text:
        return "action_reset_airport"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return [SlotSet("airport", None)]