'''
Created on Dec 9, 2018

@author: rabihkodeih
'''


EVENT_UPDATE_APP = 'EVENT_UPDATE_APP'

EVENTS = [
    EVENT_UPDATE_APP
]

HANDLERS = {event:[] for event in EVENTS}


def register(observer, event):
    HANDLERS[event].append(observer)
    
    
def fire_event(event, *args, **kwargs):
    for handler in HANDLERS[event]:
        handler(*args, **kwargs)
        

# end of file
