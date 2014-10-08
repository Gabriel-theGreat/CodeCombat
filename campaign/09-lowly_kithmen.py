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

orders =  [{'action':'move','direction':'right'},{'action':'attack'},{'action':'move','direction':'down'},{'action':'move','direction':'up'},{'action':'move','direction':'right'},{'action':'attack'},{'action':'move','direction':'down'}]

for order in orders:
    if order['action'] == 'move':
        simple_boots(order['direction'])
    elif order['action'] == 'attack':
        enemy = self.getNearestEnemy()
        longsword(enemy)
        longsword(enemy)
