# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from datetime import datetime
import random

class ActionRestarted(Action): 	
    def name(self): 		
        return 'action_restarted' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()] 
class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]
        
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
        
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        output = "Hello World!"

        dispatcher.utter_message(text=output)

        return []
        
class ActionLogCheckin(Action):

    def name(self) -> Text:
        return "action_log_checkin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        file_object = open('checkin.log', 'a')
        car_type=tracker.get_slot("car_type")
        car_color=tracker.get_slot("car_color")
        if(car_color=="" and car_type==""):
            file_object.write(tracker.get_slot("res_first_name")+" "+ tracker.get_slot("res_last_name") + " checked in with no car"+"\n")
        elif(car_color!="" and car_type!=""):
            file_object.write(tracker.get_slot("res_first_name")+" "+ tracker.get_slot("res_last_name") + " checked in with a "+car_color+" " +car_type+"\n")
        else:
            file_object.write(tracker.get_slot("res_first_name")+" "+ tracker.get_slot("res_last_name") + " checked in with a car, but we failed to get the type\n")

        return []
class ActionLogCheckoutGood(Action):

    def name(self) -> Text:
        return "action_log_checkout_good"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        file_object = open('checkout.log', 'a')
        file_object.write(tracker.get_slot("res_first_name")+" "+ tracker.get_slot("res_last_name") + " checked out of room "+tracker.get_slot("room_number"))

        return []
class ActionLogCheckoutBad(Action):

    def name(self) -> Text:
        return "action_log_checkout_bad"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        file_object = open('checkout.log', 'a')
        file_object.write(tracker.get_slot("res_first_name")+" "+ tracker.get_slot("res_last_name") + " checked out of room "+tracker.get_slot("room_number")+" but disputed the price")

        return []