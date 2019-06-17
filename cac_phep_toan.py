import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print('x = ',x)
print('y = ',y)

# Cộng hai mảng
print('x + y = ', np.add(x, y))

# Trừ hai mảng
print('x - y = ', np.subtract(x, y))

# Thực hiện phép nhân trên 2 mảng
print('x*y = ', np.multiply(x, y))

# Thực hiện phép chia trên 2 mảng
print('x/y = ',np.divide(x, y))

# Thực hiện phép khai căn bậc 2 trên mảng x
print(np.sqrt(x))

# Tổng các phần tử cua mot mang
print(np.sum(x))

# Phép toán chuyển vị:
print(x)
print (x.T)

###### Tích trong hai ma trận ######
v = np.array([9,10])
w = np.array([11,12])

print(np.dot(v, w))      # Tích trong, cho kết quả: 219 = 9.11+10.12
print(np.dot(x, v))      # Tích trong, cho kết quả: [29 67]

###### Tích của hai ma trận ######
print(np.matmul(x,y))    # Nhân hai ma trận
                          # [[19 22]
                          #  [43 50]]

print(np.matmul(x,v.T))  # Nhân hai ma trận
                          # [29 67]
print(np.matmul(v,x))    # Nhân hai ma trận
                          # [39 58]

###### Tích tương ứng (elementwise) hai ma trận ######
print(np.multiply(x,y))  # [[5 12]
                          #  [21 32]]