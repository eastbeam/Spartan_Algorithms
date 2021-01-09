numbers = [2, 3, 1]
target_number = 0

# numbers = [1, 1, 1, 1, 1]
# target_number = 3

result = []
result_count = 0

# def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
#     if current_index == len(numbers):
#         all_ways.append(current_sum)
#         return
#     get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + numbers[current_index], all_ways)
#     # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0 + 2, all_ways)
#     get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - numbers[current_index], all_ways)
#     # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0 - 2, all_ways)
#
# print(get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result))
# print(result)


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum): #target_count):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count
            result_count += 1
            # target_count += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + numbers[current_index]) #, target_count)
    # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0 + 2, all_ways)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - numbers[current_index]) #, target_count)
    # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0 - 2, all_ways)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)) #, result_count))  # 5를 반환해야 합니다!
# Call by Object Reference in Python
print(result_count)
# print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!