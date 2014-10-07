# Use a loop to both navigate and attack.

# Uncomment the variable and attack!
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

def attackNearest():
    enemy = self.getNearestEnemy()
    longsword(enemy)
    longsword(enemy)

orders =  [{'action':'move','direction':'right'},{'action':'move','direction':'up'},{'action':'attack'},{'action':'move','direction':'right'},{'action':'move','direction':'down'},{'action':'move','direction':'down'},{'action':'move','direction':'up'}]


for x in range(0, 3) :
    for order in orders:
        if order['action'] == 'move':
            simple_boots(order['direction'])
        elif order['action'] == 'attack':
            attackNearest()
simple_boots('right')
