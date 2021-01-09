input = [3, 5, 6, 1, 2, 4]

print(input[0])


def find_max_num(array):
    # 이 부분을 채워보세요!
    # for i in int:
    #     findMax = int[i]
    #     if findMax < int[i+1]:
    #         findMax = int[i+1]
    #     else:
    #         findMax = int[i]
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
