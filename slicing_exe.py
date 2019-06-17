import numpy as np

# Tạo ra mảng 2 chiều có kích thước (3, 4)
a = np.array([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
print(a)
print(a.shape)

# Truy cập vào hàng thứ 2, và tất cả các cột
row_1 = a[1,:]
print(row_1)

# Truy cập vào hàng thứ 2 và 3, và tất cả các cột
row_r2 = a[1:3, :]
print(row_r2)

# Truy cập vào cot thứ 2, và tất cả các hàng
col_r1 = a[:, 1]
print(col_r1)
print(col_r1.shape) # mang 1 chieu

# Truy cập vào cot thứ 2, và tất cả các hàng
col_r2 = a[:, 1:2]
print(col_r2)
print(col_r2.shape) # mang ba chieu (3 hang), 1 cot