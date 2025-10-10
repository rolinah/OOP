# Class for Item
class Item:
    def __init__(self, name, price):    

        self.name = name
        self.price = price


# Class for Cart
class Cart:
    def __init__(self):
        self.items = {}   # store items in dictionary {item: qty}

    def add_item(self, item, qty):
        if item in self.items:      #checks if the item exists in the cart
            self.items[item] += qty
        else:
            self.items[item] = qty

    def remove_item(self, item, qty):    
        if item in self.items:
            self.items[item] -= qty
            if self.items[item] <= 0:   # if quantity is zero or negative, remove it completely
                del self.items[item]

    def total(self):
        total_cost = 0
        for item, qty in self.items.items():
            total_cost += item.price * qty
        return total_cost

    def summary(self):
        print("\n--- CART SUMMARY ---")
        for item, qty in self.items.items():                         #loops through each item in the cart
            print(f"{item.name} (x{qty}) = {item.price * qty} UGX")
        print(f"Total Cost = {self.total()} UGX")
        print("---------------------\n")


# ---------- Testing the System ----------
# Step 1: Create items
item1 = Item("Bread", 3000)
item2 = Item("Milk", 2000)
item3 = Item("Eggs", 500)

# Step 2: Create cart and add items
cart = Cart()
cart.add_item(item1, 2)   # 2 breads
cart.add_item(item2, 3)   # 3 milks
cart.add_item(item3, 10)  # 10 eggs

# Print cart summary
cart.summary()

# Step 3: Remove 1 item (e.g., 1 milk)
cart.remove_item(item2, 1)

# Print cart again
cart.summary()