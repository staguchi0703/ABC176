def resolve():
    '''
    code here
    '''
    N, X, T = [int(item) for item in input().split()]

    if N % X != 0:
        res = (N // X + 1) * T
    else:
        res = (N // X) * T
    print(res)

    


if __name__ == "__main__":
    resolve()
