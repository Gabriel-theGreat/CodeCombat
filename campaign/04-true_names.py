# Defend against Brak and Zort!
# You must attack Munchkins twice.

#Original Code:
#self.moveRight()
#self.attack("Brak")
#self.attack("Brak")

# Evade the munchkin. Grab the gems.

# This function is put at the top, else the compiler insist on using this.simple_boots
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

orders =  [{'action':'move','direction':'right'},{'action':'attack','target':'Brak'},{'action':'attack','target':'Brak'},{'action':'move','direction':'right'},{'action':'move','direction':'right'},{'action':'attack','target':'Zort'},{'action':'attack','target':'Zort'},{'action':'move','direction':'right'}]

for order in orders:
    if order['action'] == 'move':
        simple_boots(order['direction'])
    elif order['action'] == 'attack':
        longsword(order['target'])
