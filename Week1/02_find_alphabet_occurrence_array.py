def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

    # for label in range(len(string)):
    #     if string[label].isalpha() == 1:
    #         for i in range(26):
    #             word = ord(string[label]) - (i+97)
    #             find_alphabet_occurrence_array[word] =+ 1
    #     else:
    #         continue

    # for num in alphabet_occurrence_array:
    #     for compare_num in alphabet_occurrence_array:
    #         if num < compare_num:
    #             break
    #     else:
    #         return num

    # return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))