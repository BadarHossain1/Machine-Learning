Array Manipulation

array = np.random.randint(0,10,(2,3))
print(array)
print(array.shape)
[[3 1 8]
 [4 1 7]]
(2, 3)

# transpose

trans = np.transpose(array)
print(trans)
print(trans.shape)
[[3 4]
 [1 1]
 [8 7]]
(3, 2)

array = np.random.randint(0,10,(2,3))
print(array)
print(array.shape)
[[7 0 5]
 [8 0 0]]
(2, 3)


trans2 = array.T
print(trans2)
print(trans2.shape)
[[7 8]
 [0 0]
 [5 0]]
(3, 2)


# reshaping a array

a = np.random.randint(0,10,(2,3))
print(a)
print(a.shape)
[[7 9 6]
 [1 3 4]]
(2, 3)

b = a.reshape(3,2) #2*3 = 3*2
print(b)
print(b.shape)
[[7 9]
 [6 1]
 [3 4]]
(3, 2)