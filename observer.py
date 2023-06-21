class Observer():
    def __init__(self):
        self.subscrib = []

    def subscribe(self, who, cod_event):
        self.subscrib.append({'who': who, 'event': cod_event})

    def notify(self, cod_event, value=None):
        for a in self.subscrib:
            if a['event'] == cod_event:
                a['who'](self, value,cod_event)

# [{'who':model2,'cod_event':2}]
# [{'event':2,'sub':[]}]
