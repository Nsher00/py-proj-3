import csv

class Melon:
    def __init__(self, melon_id, common_name, price, image_url, color, seedless) -> None:
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    def __repr__(self) -> str:
        """This is a method to show info about melon in console."""
        return f'<Melon: {self.melon_id}, {self.common_name}>'
    
    def price_str(self):
        '''Return the formatted price as a string'''
        return f'${self.price:.2f}'

melon_dict = {}

with open('melons.csv') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon_id = row['melon_id']
        melon = Melon(melon_id, row['common_name'], float(row['price']), row['image_url'], row['color'], eval(row['seedless']))
        melon_dict[melon_id] = melon

def get_by_id(melon_id):
        '''returns melon by unique id.'''
        return melon_dict[melon_id]

def get_all():
     '''returns a list of all the melons'''
     return list(melon_dict.values())

