def resolve():
    '''
    code here
    '''

    N = input()

    sum_num = 0
    for item in N:
        sum_num += int(item)

    if sum_num % 9 == 0:
        print('Yes')
    else:
        print('No')
