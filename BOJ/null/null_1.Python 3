/*
* 메모리: 29200 KB, 시간: 72 ms
* 타이머 시간: null
* 2021.11.08
* by Alub
**/
def atob(b, a, cnt):
    if b == a:
        print(f'{cnt}')

    if b > a:
        if b % 10 == 1:
            c = b // 10
            cnt += 1
            atob(c, a, cnt)
        else:
            c = b//2
            if c * 2 == b:
                cnt += 1
                atob(c, a, cnt)
            else:
                print('-1')

    if b < a:
        print('-1')

A, B = map(int, input().split())
atob(B, A, 1)
