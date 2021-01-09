# factorial(N) = N * factorial(N-1)
# factorial(1) = 1

def factorial(n):
    if n == 1:
        return 1

    return n*factorial(n-1)
    
    # initial = n
    # for i in range(1,n):
    #     initial = initial * i
    # # 이 부분을 채워보세요!
    # return initial


print(factorial(5))