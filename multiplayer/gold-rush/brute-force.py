items =  self.getItems()

#Early exit for the first iteration
if len(items) == 0 : 
    self.moveXY(18, 36) 
    return

target = items[0]
item_value_dictionary = {}

for item in self.getItems():
    item_value =  item.bountyGold / self.distance(item)
    item_value_dictionary[item.id]=item_value
    if item_value_dictionary[target.id] <  item_value_dictionary[item.id] :
        target = item

self.move(target.pos)
