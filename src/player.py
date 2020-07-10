# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.room = current_room
        self.items = items

    def pickup_item(self, item_list, item):
        for i in range(len(item_list)):
            if item_list[i].name == item:
                self.items.append(item_list[i])

    def drop_item(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)

    def see_inventory(self):
        for i in self.items:
            print(i.name)

    def __str__(self):
        return f"{self.name} is at {self.room}"
