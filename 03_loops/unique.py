items=["apple","banana","orange","mango","apple","mango"]

# unique_item= set()

# for ls in items:
#     print(unique_item)
#     if ls in unique_item:
#         print("Duplicate iteam is:",ls)
#         break
#     unique_item.add(ls)

# to show if list has more then one duplicate items

unique_items = set()
duplicates = set()

for item in items:
    if item in unique_items:
        duplicates.add(item)
    else:
        unique_items.add(item)

print("Duplicate items are:", list(duplicates))

