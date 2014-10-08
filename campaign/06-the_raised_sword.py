# Defeat the ogres. 
# Remember that they each take two hits.

def simple_boots(move):
    if move == 'right':
        self.moveRight()
    elif move == 'left':
        self.moveLeft()
    elif move == 'up':
        self.moveUp()
    elif move == 'down':
        self.moveDown()

def longsword(target):
    self.attack(target)

orders =  [{'action':'attack','target':'Beebop'},{'action':'attack','target':'Beebop'},{'action':'attack','target':'Ack'},{'action':'attack','target':'Ack'},{'action':'attack','target':'Smashy'},{'action':'attack','target':'Smashy'}]

for order in orders:
    if order['action'] == 'move':
        simple_boots(order['direction'])
    elif order['action'] == 'attack':
        longsword(order['target'])
