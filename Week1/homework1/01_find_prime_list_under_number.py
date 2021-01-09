input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []
    for i in range(2, number+1):
        for d in range(2, i+1):
            if (i % d) == 0:
                if i == d:
                    if i not in prime_list:
                        prime_list.append(i)
                else:
                    break

    return prime_list


result = find_prime_list_under_number(input)
print(result)