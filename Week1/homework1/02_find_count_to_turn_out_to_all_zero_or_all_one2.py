input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    else:
        count_to_all_zero += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == '0':
                count_to_all_one += 1
            else:
                count_to_all_zero += 1
        else:
            continue


    if count_to_all_one > count_to_all_zero:
        min_turn = count_to_all_zero
    elif count_to_all_one < count_to_all_zero:
        min_turn = count_to_all_one
    else:
        min_turn = count_to_all_one


    return min_turn


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)