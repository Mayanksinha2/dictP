# Dictonary is nothing but a key value pair
d1 = {
    'Manku':'Litti',
    'Sonu':'Samosa',
    'Rahul':'Biryani',
    420: 'pani',
}
print(d1)
print(d1["Sonu"])
d1['Ankit'] = "Junk Food"
print(d1)
del d1['Rahul']
print(d1)

d2 = d1.copy()
del d2['Sonu']
print(d2)

d1.update({'Lila':'icecream'})
print(d1)
print(d1.keys())
print(d1.items())