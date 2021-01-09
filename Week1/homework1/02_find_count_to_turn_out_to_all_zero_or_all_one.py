input = "011010"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    bit_array = [0]*2
    bit_save = 0

    for elem in list(string):
        if elem == 0:
            bit_array[0] += 1
        else:
            bit_array[1] += 1

        for i in range(len(string)):
            print(i)
            if not elem[i] == elem[i+1]:
                stamp_bit += 1

    if stamp_bit == 0:
        min_turn = 1
    else:
        min_turn = stamp_bit - 1

    return min_turn


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)