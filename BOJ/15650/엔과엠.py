/*
* 메모리: 29200 KB, 시간: 68 ms
* 타이머 시간: null
* 2021.11.13
* by Alub
**/
N, M = map(int, input().split())


def permute(num, cnt, result: list):
    if cnt == M :
        print(' '.join(result))
    elif num > N:
        return
    elif cnt < M:
        next_result = result + [str(num)]
        permute(num+1, cnt + 1, next_result)
        permute(num + 1, cnt, result)



result = []
permute(1, 0, result)
