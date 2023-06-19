

class Observer():
    def __init__(self):
        self.subscribers={}
    def reg_event(self,cod_event):
        self.cod_event=cod_event


    def subscribe(self,cod_event,who):
        self.subscribers['subscr']=who

