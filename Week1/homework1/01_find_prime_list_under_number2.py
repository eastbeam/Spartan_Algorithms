input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []
    for i in range(2, number+1):
        for d in range(2, i):
            if (i % d) == 0:
                break
        else:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)