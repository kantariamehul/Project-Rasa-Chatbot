from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from requests.models import Response
from Email import insert_email
from Admission import insert_adm
from Weather import Weather_fun
from Math import Math_is_fun

class Save_MU_stu(Action):
    def name(self) -> Text:
        return "action_email_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        em=tracker.get_slot("email")
        enr=tracker.get_slot("enrollment")

        #dispatcher.utter_message(text="Email and Enrollment are")
        #dispatcher.utter_message(tracker.get_slot("enrollment"))
        #dispatcher.utter_message(tracker.get_slot("email"))

        dispatcher.utter_message(text="Data storing in Data base")
        insert_email(em, enr)
        dispatcher.utter_message(text="Sucessfully saved data in Data base")
        return []

class Save_ADM_stu(Action):
    def name(self) -> Text:
        return "action_adm_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nam=tracker.get_slot("name")
        sur=tracker.get_slot("surname")
        res=tracker.get_slot("result")
        cit=tracker.get_slot("city")
        mob=tracker.get_slot("mobile")
        cou=tracker.get_slot("course")
        edu=tracker.get_slot("education")
        deg=tracker.get_slot("degree")
        bra=tracker.get_slot("branch")

        dispatcher.utter_message(text="Data storing in Data base")
        insert_adm(nam,sur,res,cit,mob,cou,edu,deg,bra)
        dispatcher.utter_message(text="Sucessfully saved data in Data base")
        return []

class MU_Weather(Action):
    def name(self) -> Text:
        return "action_weather_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="In case you are planning to visit MU now,")
        tracker.slots["Rajkot_weather"] = Weather_fun()
        print(tracker.get_slot("Rajkot_weather"))
        dispatcher.utter_message(response="action_weather_data",Rajkot_weather=tracker.get_slot("Rajkot_weather"))
        return []

class MU_Math(Action):
    def name(self) -> Text:
        return "action_math_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Lets have fun")
        tracker.slots["Math_prob"] = Math_is_fun()
        print(tracker.get_slot("Math_prob"))
        dispatcher.utter_message(response="action_math_data",Math_prob=tracker.get_slot("Math_prob"))
        return []