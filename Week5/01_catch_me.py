from collections import deque

c = 11 # 12 / 14 / 17 / 21 / 26
b = 2  # 4 / 8 / 16 / 32


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0

    queue = deque()
    queue.append((brown_loc, 0)) # (position, time)

    visited = [{} for _ in range(200001)]
    # visited[2] = {2: True, 0: True}

    while cony_loc <= 200000:
        cony_loc += time

        if time in visited[cony_loc]:
            return time


        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_position = current_position - 1
            if new_position >=0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position <= 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position <= 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1

    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!