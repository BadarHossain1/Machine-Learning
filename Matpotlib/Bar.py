fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
languages = ['English', 'Bangla', 'Hindi', 'Arabic', 'Urdu']
people = [100, 80, 60, 45, 20]
ax.bar(languages, people)
ax.xlabel('Languages')
ax.ylabel = ('Number of people')
ax.title('Popularity of languages')
plt.show()

