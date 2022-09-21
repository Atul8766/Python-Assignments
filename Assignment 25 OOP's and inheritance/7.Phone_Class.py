class Phone:
    def __init__(self,call,sms):
        self.call = call
        self.sms = sms
    def display(self):
        print(self.call)
        print(self.sms)

ph1 = Phone('VoLTE','Media')

ph1.display()
