current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#      N  E  S  W
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4

def get_d_index_when_go_back(d):
    return (d + 2) % 4

# BFS

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])

    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = list([[r, c, d]])

    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                room_map[new_r][new_c] = 2
                count_of_departments_cleaned += 1
                queue.append([new_r, new_c, temp_d])
                break

            elif i == 3:
                new_r, new_c = r + dr[get_d_index_when_go_back(temp_d)], c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])
                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned



# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))

## 후진을 못하는 상태 (if room_map[new_r][new_c] != 0:)
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#  [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#  [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#  [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#  [1, 0, 0, 2, 2, 0, 0, 0, 0, 1],
#  [1, 0, 2, 2, 2, 2, 0, 1, 0, 1],
#  [1, 2, 2, 2, 2, 2, 1, 1, 0, 1],
#  [1, 2, 2, 2, 2, 2, 1, 1, 0, 1],
#  [1, 0, 2, 2, 2, 2, 0, 0, 0, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

## 후진을 해도 뒤가 벽인 상태 (정답)
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
#  [1, 2, 2, 2, 1, 1, 1, 1, 2, 1],
#  [1, 2, 2, 1, 1, 2, 2, 2, 2, 1],
#  [1, 2, 1, 1, 2, 2, 2, 2, 0, 1],
#  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
#  [1, 2, 2, 2, 2, 2, 0, 1, 2, 1],
#  [1, 2, 2, 2, 2, 2, 1, 1, 2, 1],
#  [1, 2, 2, 2, 2, 2, 1, 1, 2, 1],
#  [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]