def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    res = 0
    if N >= 2:
        prev = As[0]
        for item in As[1:]:
            if item < prev:
                res += prev - item
            else:
                prev = item

    else:
        res = 0

    print(res)

if __name__ == "__main__":
    resolve()
