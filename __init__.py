from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder

# Import database.py
import sys
from os.path import dirname, abspath
sys.path.append(dirname(abspath(__file__)))
from database import Database


class MedicationAlarm(MycroftSkill):
    """
    Medication Alarm is a simple utility for managing medication dosing with My
        croft.

    Terminology:
        medID     Unique identifier for a specific medication dosing schedule.
        name      Medication name
        dose      Real Number
        doseUnit  Define the unit of measurement used in dose
        maxDose   maximum units taken in interval
        interval  frequency of dosing
        idt       Interval Display Type
        lastTake  Last time the medication was taken.
        nextAvail The next time the medication can be taken
        alarmOpt  Alarm type


    Class methods:
        read    Allows you to read details on a medication value across
            matching names
        list    Allows you to read medication names as a list
        add     Allows you to add new lists or new items to existing lists.
        del     Allows you to delete a list or an item from a list.
        edit    Allows you to change data stored.
    """

    def __init__(self):
        MycroftSkill.__init__(self)
        self.db = Database()

    @intent_handler(IntentBuilder('list'))
    def handle_list(self, message):


def create_skill():
    return MedicationAlarm()
