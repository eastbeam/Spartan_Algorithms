input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n -1 -i]:
            return False

    return True

    # My Initial Guess
    # init = 0
    # fine = len(string) -1
    # middle = len(string) // 2
    #
    # for i in range(middle):
    #     if string[init] == string[fine]:
    #         init += 1
    #         fine -= 1
    #         continue
    #     else:
    #         return False
    # return True


print(is_palindrome(input))