# numbers = [2, 3, 1]
# target_number = 0

numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    plus_minus = 0
    count_opr = 0
    for opr in array:
        if opr > target:
            plus_minus -= opr
            count_opr += 1
        else:
            plus_minus += opr
            count_opr += 1

    return count_opr


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!