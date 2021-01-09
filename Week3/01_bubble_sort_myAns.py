input = [4, 6, 2, 9, 1]

dim_array = len(input) - 1

def bubble_sort(array):
    # 이 부분을 채워보세요!
    global dim_array

    for i in range(dim_array):
        for j in range(i+1,i+2):
            print(array[i], array[j])
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                i += 1
                if i == dim_array:
                    dim_array -= 1
                    bubble_sort(array)
            else:
                i += 1
                if i == dim_array:
                    dim_array -= 1
                    bubble_sort(array)

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!