shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# def is_existing_target_number_binary(target, array):
#     current_min = 0
#     current_max = len(array) - 1
#     current_guess = (current_min + current_max) // 2
#     # find_count = 0
#
#     while current_min <= current_max:
#         # find_count += 1
#         if array[current_guess] == target:
#             # print(find_count)
#             return True
#         elif array[current_guess] < target:
#             current_min = current_guess + 1
#         else:
#             current_max = current_guess - 1
#         current_guess = (current_min + current_max) // 2
#
#     # 구현해보세요!
#     return False
#
#
# def is_available_to_order(menus, orders):
#     # 이 부분을 채워보세요! O{(M+N)*logN}
#     shop_menus.sort() # 정렬의 시간 복합도는 배열의 길이가 N이라고 할 때 O(N*logN)
#     for order in orders: # O(M*logN)
#         if not is_existing_target_number_binary(order,shop_menus): # O(logN)
#             return False
#     return True


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요! O(N+M)
    menus_set = set(menus) # O(N)
    for order in orders: # M
        if order not in menus_set: # O(1)
            return False
        else:
            return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)