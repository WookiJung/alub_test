/*
* 메모리: 29200 KB, 시간: 76 ms
* 타이머 시간: null
* 2021.11.12
* by Alub
**/
S = input()
T = input()
len_T = len(T)

def atob(T):
    global ans
    for i in range(len_T - 1, len(S) - 1, -1):

        if T[i] == 'A':
            T = T[:len(T)-1]
        elif T[i] == 'B':
            T = T[len(T)-2::-1]

    if T == S:
        ans = 1
    else:
        ans = 0
    return ans


ans = 1

atob(T)
print(ans)