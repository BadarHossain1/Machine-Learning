x = np.linspace(0,10,100) 
y = np.sin(x)
z = np.cos(x)

print(x)
print(y)
print(z)

Plotting the data

# sine wave

plt.plot(x,y)
plt.show()

# cosine wave

plt.plot(x,z)
plt.show()

# adding title x-axis & y-axis labels

plt.plot(x,y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()


# parabola 

x = np.linspace(-10,10,20)
y = x**2
plt.plot(x,y)
plt.title('Parabola')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(x,y,'r+')
plt.show()

x = np.linspace(-5,5,50)
plt.plot(x, np.sin(x), 'gx')
plt.plot(x, np.cos(x), 'r+')

