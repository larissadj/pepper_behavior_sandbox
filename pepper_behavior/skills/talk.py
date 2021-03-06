import rospy
import smach


class Talk(smach.State):
    def __init__(self, controller, id=None, text=None, textblock='greeting'):
        self.id = id
        self.textblock = textblock
        self.text = text
        if self.textblock == 'greeting':
            self.text = ['Hi! Ich bin Pepper. Mit mir wird zur Zeit am ceitaek der Universität Bielefeld geforscht.',
                         'Willkommen auf der Messe. Mein Name ist Pepper.',
                         'Hallo zusammen, ich bin Pepper! Ich freue mich hier zu sein.',
                         'Hallo Leute! Ich unterstütze derzeit die Forschung am ceitaek der Uni Bielefeld.',
                         'Herzlich Willkommen, mein Name ist Pepper ich bin ein Roboter vom ceitaek der Uni Bielefeld.']
        elif self.textblock == 'answer':
            self.text = [
                'Mir geht es sehr gut. Ich freue mich heute dabei zu sein.',
                'Ich wurde von Softbank Robotics gebaut. Zur Zeit werde ich am ceitaek der Universität Bielefeld weiter entwickelt.',
                'Ich bin ein sozialer Roboter, der auf die Interaktion mit Menschen spezialisiert ist.',
                'Wir zeigen Ihnen auf der Messe, wie smarte, innovative Lösungen Ihr Unternehmen für '
                'die digitale Zukunft vorbereiten.',
                'Ich habe Sie leider nicht verstanden.',
                'Ich habe Sie leider nicht verstanden.',
                'Ich habe Sie leider nicht verstanden.',
                'Ich habe Sie leider nicht verstanden.']
        else:
            self.text = ['Ich mache gleich mal weiter. Für Demos schauen Sie bitte dort drüben.',
                         'Ich gucke gleich weiter nach Gästen. Werfen Sie nach den Vorträgen einen Blick in die Ausstellung. Genau dort.',
                         'Reden Sie nachher mit mir, in der Ausstellung. Dort hinten.',
                         'Wir haben dieses Jahr wieder eine Menge Demos. In dieser Richtung bitte.',
                         'Unterhalten Sie sich nach den Vorträgen doch mit mir in der Ausstellung. Dahinten. Bis nachher.']
        self.say = text
        if self.id:
            input_k = []
        else:
            input_k = ['id']
        smach.State.__init__(self, outcomes=['success'], input_keys=input_k)
        self.talk = controller

    def execute(self, userdata):
        if self.id:
            talk = self.text[self.id]
        elif self.say:
            talk = self.say
        else:
            talk = self.text[userdata.id]
        result = self.talk.say_something(talk)
        return result
