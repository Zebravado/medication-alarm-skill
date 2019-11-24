from mycroft import MycroftSkill, intent_file_handler


class MedicationAlarm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('alarm.medication.intent')
    def handle_alarm_medication(self, message):
        self.speak_dialog('alarm.medication')

    #loads medications from the listed file and returns the list of all medication as a Dictonary of arrays.
    def load_medications_and_timers_from_file(self, fileName):
        medicationsFile = open(fileName, "r")
        medList = {}
        count = 0
        name = "This Should not be seen"
        nextDue = 0
        interval = 0
        intervalDisplayType = 0
        line
        while True:
            try:
                line = medicationsFile.readline()
                comma = line.index(',#,')
                name = line[0:comma]
                line = line[comma+2:]
                nextDue = int(line[0:comma])
                line = line(comma+2:)
                interval = int(line[0:comma])
                line = line(comma+2:)
                intervalDisplayType = int(line[0:comma])
                medList[count] = [name,nextDue,interval,intervalDisplayType]
                count++
            except:
                break
        return medList

def create_skill():
    return MedicationAlarm()

