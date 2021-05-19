from mycroft import MycroftSkill, intent_file_handler


class Lavarlegumes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lavarlegumes.intent')
    def handle_lavarlegumes(self, message):
        self.speak_dialog('lavarlegumes')


def create_skill():
    return Lavarlegumes()

