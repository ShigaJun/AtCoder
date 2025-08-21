S = input()
T = input()
S_list = []
T_list = []

cnt = 1
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        cnt += 1
    else:
        S_list.append([S[i], cnt])
        cnt = 1
S_list.append([S[-1], cnt])

cnt = 1
for i in range(len(T) - 1):
    if T[i] == T[i + 1]:
        cnt += 1
    else:
        T_list.append([T[i], cnt])
        cnt = 1
T_list.append([T[-1], cnt])

if len(S_list) != len(T_list):
    print("No")
    exit()
for i in range(len(T_list)):
    if S_list[i][0] != T_list[i][0] or T_list[i][1] < S_list[i][1] or (T_list[i][1] > S_list[i][1] and S_list[i][1] == 1):
        print("No")
        break
else:
    print("Yes")