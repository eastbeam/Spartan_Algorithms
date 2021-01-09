input = "abaabadce"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    # for index in range(len(alphabet_occurrence_array)):
    #     if alphabet_occurrence_array[index] == 1:
    #         alphabet_occurrence = chr(index+ord('a'))
    #         break
    #
    #     else:
    #         alphabet_occurrence = '_'

    not_repeating_character_array = []

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
                not_repeating_character_array.append(chr(index+ord('a')))
                # min_alphabet = not_repeating_character_array[0]

    for char in string:
        if char in find_not_repeating_character:
            return char


    return '_'

    # return alphabet_occurrence


result = find_not_repeating_character(input)
print(result)