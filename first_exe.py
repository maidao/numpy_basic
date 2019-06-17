import numpy as np

a = np.array([1,2,3]) # Tạo ra mảng một chiều từ list
print(a) # [1 2 3]
print(type(a)) # <class 'numpy.ndarray'>

print(a.shape) # (3,) --> mang 1 chieu, 3 phan tu
a[0] = 5 # sua gia tri phan tu [0] cua mang tu 1 --> 5
print(a) # [5 2 3]

# Tạo ra mảng hai chiều từ 2 list
b = np.array([[1,2,3],[4,5,6]]) # trong mot mang co 2 list
print(b)
print(b.shape) # ( 2, 3) --> mang hai chieu (2 dong), moi dong 3 phan tu (3 cot)
print(b.size) # 6 ---> số phần từ trong mảng
print(b[0,0],b[0,1]) # 1 2 ---> in ra phan tu (hang O, cot 0) = 1, va phan tu (hang 0, cot 1) = 2 cua mang b

# Tạo ra mảng trong khoảng cho trước
c = np.arange(0,3)
print(c) # [0 1 2]

# Tạo ra mảng toàn số 0
d = np.zeros((2,3)) # mang d co shape la (2,3) = 2 hang, 3 cot toan phan tu 0
print(d)

# Tạo ra mảng toàn số 1
e = np.ones((1,2))# mang e co shape la (1,2) = 1 hang, 2 cot toan phan tu 1
print(e)

# Tạo ra một mảng hằng số
f = np.full((2,4),7) # mang f co shape la (2,4) = 2 hang, 4 cot toan phan tu 7
print(f)

# Tạo ma trận đơn vị 2x2 --> la ma tran vuong (so hang = so cot), hang cheo matran = 1
g = np.eye(2)
print(g)

# Tạo ma trận 2x2, giá trị ngẫu nhiên trong khoang (0,1)
h = np.random.random((2,2))
print(h)