n, q = map(int, input().split())
a = list(map(int, input().split()))
max_val = 10 ** 6
accum_sum = [0] * (max_val + 1)
accum_cnt = [0] * (max_val + 1)
for i in range(n):
    accum_sum[a[i]] += a[i]
    accum_cnt[a[i]] += 1
for i in range(1, max_val + 1):
    accum_sum[i] += accum_sum[i - 1]
    accum_cnt[i] += accum_cnt[i - 1]
max_a = max(a)
for i in range(q):
    b = int(input())
    if b > max_a:
        print(-1)
    else:
        ans = accum_sum[b - 1] + (b - 1) * (n - accum_cnt[b - 1]) + 1
        print(ans)