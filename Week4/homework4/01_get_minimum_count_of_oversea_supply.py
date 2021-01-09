import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    heap = []

    idx_dates = 0
    idx_supplies = 0
    buy_count = 0

    dates.append(k)
    supplies.append(0)

    for days in range(k-1):
        stock -= 1
        if days in dates:
            saves = dates[idx_dates+1] - dates[idx_dates]
            if stock + saves < supplies[idx_supplies]:
                stock += supplies[idx_supplies]
                buy_count += 1
            else:
                continue

    return buy_count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))

# heap = []
# heapq.heappush(heap, 4)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 7)
# heapq.heappush(heap, 3)
# min = heapq.heappop(heap)

# heapq.heappush(heap, 4*-1)
# heapq.heappush(heap, 1*-1)
# heapq.heappush(heap, 7*-1)
# heapq.heappush(heap, 3*-1)
# max = heapq.heappop(heap) * -1

# print(heap, min)

## Tutorial

# ramen_stock = 4
# supply_dates = [4, 10, 15]
# supply_supplies = [20, 5, 10]
# supply_recover_k = 30
#
# def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
#     # 풀어보세요!
#     idx_dates = 0
#     buy_count = 0
#     dates.append(k)
#     supplies.append(0)
#
#     for days in range(k - 1):
#         stock -= 1  # 1. 날짜가 진행되면서 재고를 하나씩 깐다.
#         if days in dates:  # 2. 공급날이 오면
#             # 다음 공급날까지 필요한 양을 계산한다.
#             saves = dates[idx_dates + 1] - dates[idx_dates]
#             # 재고에서 다음 공급날까지 필요한 양을 빼서 음수가 나오면 무조건 이번 공급날에 받아야한다.
#             if stock - saves < 0:
#                 stock += supplies[idx_dates]  # 재고 더해주기
#                 buy_count += 1  # 구매 횟수 더하기
#             idx_dates += 1  # 공급날 인덱스 더해주기
#
#     return buy_count
#
# print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))