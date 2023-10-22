class Inventory:
    def __init__(self):
        self.inventory_list = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory_list:
            self.inventory_list[item_name] += quantity
            print(f"UPDATED Item {item_name}")
        else:
            self.inventory_list[item_name] = quantity
            print(f"ADDED Item {item_name}")

    def delete_item(self, item_name, quantity):
        if item_name not in self.inventory_list:
            print(f"Item {item_name} does not exist")
        else:
            current_quantity = self.inventory_list[item_name]
            if current_quantity < quantity:
                print(f"Item {item_name} could not be DELETED")
            else:
                self.inventory_list[item_name] -= quantity
                print(f"DELETED Item {item_name}")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory_list.items():
            print(f"{item}: {quantity}")