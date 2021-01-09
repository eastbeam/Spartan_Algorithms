input = [4, 6, 2, 9, 1]


def bubble_sort(array): # O(N^2)
    # 이 부분을 채워보세요!
    n = len(array)

    for i in range(n - 1): # O(N)
        for j in range(n - i - 1): # O(N)
            # print(array[i], array[j])
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!