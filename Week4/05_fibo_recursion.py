input = 20


def fibo_recursion(n):
    # 구현해보세요! My Ans
    # init_array = [1, 1]
    # for f in range(2, n):
    #     fibo_cell = init_array[f-1] + init_array[f-2]
    #     init_array.append(fibo_cell)
    # return init_array[n - 1]
    
    if n == 1 or n == 2:
        return 1

    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765