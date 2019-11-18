from mycroft import MycroftSkill, intent_file_handler


class MedicationAlarm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alarm.medication.intent')
    def handle_alarm_medication(self, message):
        self.speak_dialog('alarm.medication')


def create_skill():
    return MedicationAlarm()

