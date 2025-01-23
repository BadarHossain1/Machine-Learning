Scatter Plot

x = np.linspace(0,10,30)
y = np.sin(x)
plt.scatter(x,y)
plt.show()

x = np.linspace(0,10,30)
y = np.sin(x)
z = np.cos(x)
fig2 = plt.figure()
ax = fig2.add_axes([0,0,1,1])
ax.scatter(x,y, color = 'r')
ax.scatter(x,z, color = 'b')
plt.show()




3D Scatter Plot

ax = plt.axes(projection = '3d')
z = 20*np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x,y,z, c = z, cmap = 'Blues')
plt.show()

