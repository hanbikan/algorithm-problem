import sys
input = sys.stdin.readline

N, M = map(int, input().split())
small_rocks = set()
for _ in range(M):
    small_rocks.add(int(input()) - 1)

jump_to_moved_by_position = [{} for _ in range(N)]
jump_to_moved_by_position[0][0] = 0

for pos in range(N):
    for jump, moved in jump_to_moved_by_position[pos].items():
        next_positions = [
            pos + jump,
            pos + jump + 1,
        ]
        if jump - 1 >= 1:
            next_positions.append(pos + jump - 1)

        next_moved = moved + 1
        for next_pos in next_positions:
            if next_pos in small_rocks or next_pos >= N:
                continue
            next_jump = next_pos - pos
            if not jump_to_moved_by_position[next_pos].get(next_jump):
                jump_to_moved_by_position[next_pos][next_jump] = next_moved
            else:
                jump_to_moved_by_position[next_pos][next_jump] = min(jump_to_moved_by_position[next_pos][next_jump], next_moved)

result = -1
if len(jump_to_moved_by_position[-1]) != 0:
    result = min(jump_to_moved_by_position[-1].values())
print(result)