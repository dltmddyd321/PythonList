import numpy as np

a = np.array([[3,2,-1],[44,6,0],[5,-32,8]])
print(a)
print(a[2,1],a[-1,2],a[0,-2])

# 모든 행에 대해 1 이상 인덱스 값 출력
print(a[:,1:])

print(a[:,:2])

print(a[1,2],a[1][2])

print(a[:,2],a[:][2])

#세로 합계
print(a.sum(axis=0))

#가로 합계
print(a.sum(axis=1))

#왼쪽 시프트 x2 x(1) 
print(np.left_shift(a,1))

n = np.array([[1,2,3,4],[0,1,3,4],[-1,9,2,1]])
b = np.array([[1,1,2,3]])
print(n+b)
