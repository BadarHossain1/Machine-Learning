np_array = np.array([1,2,3,4,5])
print(np_array)
type(np_array)
np_array.shape
[1 2 3 4 5]
(5,)

np_array2 = np.array([(1,2,3,4,5), (6,7,8,9,10)],dtype=float)
print(np_array2)
np_array2.shape
[[ 1.  2.  3.  4.  5.]
 [ 6.  7.  8.  9. 10.]]
(2, 5)


Initial Placeholders in NumPy

x = np.zeros((4,5))
print(x)
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]

y = np.ones((3,3))
print(y)
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]


z = np.full((5,4),5)
print(z)
[[5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]
 [5 5 5 5]]



k = np.eye(4)
print(k)
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]


# create a numpy array with random values (Between 0 and 1)

b = np.random.random((3,4))
print(b)
[[0.83717053 0.21721435 0.22240814 0.83555989]
 [0.18185096 0.4921462  0.02817943 0.97134436]
 [0.22329403 0.8610448  0.50685552 0.57006662]]




# random integer values arrays within a specific range

c = np.random.randint(10,100,(3,5))
print(c)
[[21 27 16 72 73]
 [71 52 21 45 51]
 [46 45 74 51 64]]


# array of evenly space --> Specifying the number of values required

d = np.linspace(10,30,6)
print(d)
[10. 14. 18. 22. 26. 30.]


# array of evenly spaced values --> Specifying the step

e = np.arange(10,30,5)
print(e)
[10 15 20 25]


# convert a list to numpy array

list2 = [10,20,30,40,50]

np_array = np.asarray(list2)
print(np_array)
type(np_array)
[10 20 30 40 50]
numpy.ndarray


Analyzing a numpy array

c = np.random.randint(10,90,(5,5))
print(c)
[[26 17 27 37 60]
 [18 67 11 62 86]
 [57 27 74 29 84]
 [87 24 76 77 14]
 [19 78 59 16 10]]


# array dimension

print(c.shape)
(5, 5)

# number of d

print(c.ndim)
2

# number of elements in an array

print(c.size)
25


# checking the data type of the values in the array

print(c.dtype)
int64


