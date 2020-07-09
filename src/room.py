# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name 
        self.description = description
        self.items = items

    def add_item(self, i):
        self.items.append(i)

    def remove_item(self, i):
        if len(self.items) > 1:
            for i in range(len(self.items)):
                if self.items[i].name == i:
                    self.items.remove(self.items[i])
                break
        else:
            for i in range(len(self.items)):
                if self.items[i].name == i:
                    self.items.remove(self.items[i])

    def __repr__(self):
        def all_items():
            item_list = []
            if len(self.items) > 0:
                for i in range(len(self.items)):
                    item_list.append(self.items[i])
            else:
                return 'there are no items'
        return f'You are at the {self.name}, {self.description} and there is a {all_items()}' 
