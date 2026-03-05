import json

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# ---------- Task 1: Read the inventory ----------
with open("inventory.json", "r", encoding="utf-8") as file:
    inventory = json.load(file)

print(f"Total books currently in the file: {len(inventory)}")

# # ---------- Task 2: Update and save ----------
# inventory.append(new_book)

# with open("inventory.json", "w", encoding="utf-8") as file:
#     json.dump(inventory, file, indent=4)

# # ---------- Task 3: Display the updated inventory ----------
# with open("inventory.json", "r", encoding="utf-8") as file:
#     updated_inventory = json.load(file)

# for book in updated_inventory:
#     print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']:.2f}")
