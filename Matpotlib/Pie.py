Pie Chart

fig1 = plt.figure()
ax = fig1.add_axes([0,0,1,1])
languages = ['English', 'Bangla', 'Hindi', 'Arabic', 'Urdu']
people = [100, 80, 60, 45, 20]
ax.pie(people, labels = languages, autopct = '%1.2f%%') # How many decimal points we need. 
plt.show()

