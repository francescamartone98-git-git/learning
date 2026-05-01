shopping = []

item = ""
while item != "done":
    item = input("Add an item (or type 'done' to finish): ")
    if item != "done":
        shopping.append(item)

print(f"\nYou have {len(shopping)} items:")
for counter, item in enumerate(shopping, 1):
    print(f"{counter}. {item}")