/*
* 메모리: 29200 KB, 시간: 68 ms
* 타이머 시간: 00:00:10
* 2021.11.18
* by Alub
**/
N = int(input())
result = 0
for n in range(1,N+1):
    if n % 5 == 0:
        result += 1
        if n % 25 == 0:
            result += 1
            if n % 125 == 0:
                result += 1

print(result)
