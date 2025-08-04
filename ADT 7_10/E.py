import numpy as np
l = ['0', '2', '4', '6', '8']
n = int(input()) - 1
m = str(np.base_repr(n, 5))
ans = ''
for i in range(len(m)):
    ans += l[int(m[i])]
print("".join(ans))