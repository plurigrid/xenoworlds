   class Agent:
       def __init__(self, name, position):
           self.name = name
           self.position = position

       def move(self, new_position):
           self.position = new_position

       def interact(self, element):
           # ... code to interact with an element ...