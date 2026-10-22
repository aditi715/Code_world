flowers= ["rose","rose", "sunflower", "lilly", "lotus"]
print(flowers)

#Append an item 
flowers.append("tulip")
print(flowers)

# Insert an item 
flowers.insert(2,"marygold")
print(flowers)

# Remmove an item 
flowers.remove("sunflower")
print(flowers)

#Pop last item 
flowers.pop()
print(flowers)

#check if the item exist
print("rose" in flowers)

#Index of an item 
print(flowers.index("rose"))

#sort the list 
flowers.sort()
print(flowers)

#extend the list
flowers.extend(["kiwi", " apple"])
print(flowers)

c= flowers.count("rose")
print(flowers, c)

