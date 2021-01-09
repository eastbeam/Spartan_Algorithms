input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요충분 조건은
# N이 N의 제곱근 보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하게 되는데, 몫과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하이기 때문이다.
def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []
    for i in range(2, number+1):
        for d in prime_list:
            if (i % d) == 0 and d * d <= i:
                break
        else:
            prime_list.append(i)

    return prime_list


result = find_prime_list_under_number(input)
print(result)