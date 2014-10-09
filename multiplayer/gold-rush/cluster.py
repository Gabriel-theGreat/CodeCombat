items =  self.getItems()

#Early exit for the first iteration
if len(items) == 0 : 
    self.moveXY(18, 36) 
    return

target = items[0]
item_ranking = {}

for item in self.getItems():
    for neighbor in self.getItems():
        if item.distance == 0:
            neighbor_value = 1
        else:    
            neighbor_value = neighbor.bountyGold / item.distance(neighbor)
        item_ranking[item] = item_ranking[item] + neighbor_value
    item_value =  item.bountyGold / self.distance(item)
    item_ranking[item.id]=item_value
    if item_ranking[target.id] <  item_ranking[item.id] :
        target = item     
self.move(target.pos)
