shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    # shop_prices & user_coupons Sorting w/ ascending

    prices.sort(reverse=True)
    # p = len(prices)
    # for i in range(p - 1): # O(N)
    #     for j in range(p - i - 1): # O(N)
    #         if prices[j] < prices[j+1]:
    #             prices[j], prices[j+1] = prices[j+1], prices[j]

    coupons.sort(reverse=True)
    # c = len(coupons)
    # for k in range(c - 1):  # O(N)
    #     for l in range(c - k - 1):  # O(N)
    #         if coupons[l] < coupons[l + 1]:
    #             coupons[l], coupons[l + 1] = coupons[l + 1], coupons[l]

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.