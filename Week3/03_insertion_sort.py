input = [4, 6, 2, 9, 1]


def insertion_sort(array): # O(N^2) ~ Omega(N) w/ break
    # 이 부분을 채워보세요!
    n = len(array)

    for i in range(1, n):
        for j in range(i):
            print(i - j)
            if array[i - j -1] > array[i - j]:
                array[i - j -1], array[i - j] = array[i - j], array[i -j -1]
            else:
                break # O(N) 만큼 줄일 수 있는 가능성이 있음

    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!