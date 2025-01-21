Mathematical Operations

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1 + list2) # concatenate or joins two list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


a = np.random.randint(0,10,(3,3))
b = np.random.randint(10,20,(3,3))
print(a)
print(b)

[[7 6 3]
 [7 6 8]
 [0 0 1]]
[[19 18 13]
 [13 10 14]
 [19 13 18]]


# Element wise operation
print(a+b)
print(a-b)
print(a*b)
print(a/b)
[[26 24 16]
 [20 16 22]
 [19 13 19]]
[[-12 -12 -10]
 [ -6  -4  -6]
 [-19 -13 -17]]
[[133 108  39]
 [ 91  60 112]
 [  0   0  18]]
[[0.36842105 0.33333333 0.23076923]
 [0.53846154 0.6        0.57142857]
 [0.         0.         0.05555556]]


print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
[[26 24 16]
 [20 16 22]
 [19 13 19]]
[[-12 -12 -10]
 [ -6  -4  -6]
 [-19 -13 -17]]
[[133 108  39]
 [ 91  60 112]
 [  0   0  18]]
[[0.36842105 0.33333333 0.23076923]
 [0.53846154 0.6        0.57142857]
 [0.         0.         0.05555556]]


