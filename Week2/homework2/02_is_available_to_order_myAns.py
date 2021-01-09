shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus_sorted = sorted(menus)
    orders_sorted = sorted(orders)
    # print(menus)
    # print(menus_sorted)

    # menus_sorted = menus.sort()
    # print(menus)
    # print(menus_sorted)
    # print(len(menus_sorted))

    count = 0

    for ord in range(len(orders_sorted)):
        orders_count = len(orders_sorted)
        item = orders_sorted[ord]

        if menus_sorted.index(item) is not False:
            count += 1
            if count == orders_count:
                return True
            else:
                continue
        else:
            return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)