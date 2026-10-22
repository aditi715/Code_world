dict = {'Name': "Aditi", 'age' : " 19", 'college' : "UMIT"}
print(dict)
dict['City'] = " Mumbai"
print(dict)
print(dict.keys())
print(dict.items())
print(dict.values())
print("--------------------")

for key in dict:
    print(key)

for values in dict:
    print(values) 

print("--------------------")       

for key, values in dict.items():
    print(key, values)    

for key, values in dict.items():
    print(key,":" ,values) 

print("--------------------")         

# update

dict.update({'age': " 20"})
print(dict)

#copy dict
dict_copy = dict.copy()
print(dict_copy)

#delete key and value
del dict_copy['age']
print(dict_copy)

#printing any key and value

print('Name' in dict )
print('age' in dict_copy)

# adding multiple values
dict ={ 'Name': "Mayuresh", 'fav cuisin': "[ chineese, Indian]", 'food': "[Biryani, Panipuri]"}
print(dict)

#printing specific value 
print(dict['fav cuisin'][0])  # not woring properly

dict.clear()
print(dict)