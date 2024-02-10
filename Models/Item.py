import json
class Item:
    def __init__(self, id, name, price, category, picture):
        self.id = id
        self.category = category
        self.name = name
        self.price = price
        self.picture = picture

    def to_json(self):
        item_data = {
            'id': str(self.id),
            'category': self.category,
            'name': self.name,
            'price': self.price,
            'picture': self.picture
        }
        return item_data
