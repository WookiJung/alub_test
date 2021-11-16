/*
* 메모리: 44160 KB, 시간: 184 ms
* 타이머 시간: null
* 2021.11.16
* by Alub
**/
for tc in range(int(input())):
    p = input()
    N = int(input())
    array = input()
    array_num = array[1:len(array) - 1].split(',')

    p = p.replace('RR', '')

    r = 0
    s, e = 0, 0
    for i in p:
        if i == 'R':
            r += 1
        elif i == 'D':
            if r % 2 == 0:
                s += 1
            else:
                e += 1
                
    if s + e <= N:
        result = array_num[s:N-e]
        if r % 2:
            print('[' + ','.join(result[::-1]) + ']')
        else:
            print('[' + ','.join(result) + ']')
    else:
        print('error')
