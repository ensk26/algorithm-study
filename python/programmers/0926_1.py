#다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    total = 0
    left = 0
    right = 0
    time = 0
    q = deque()
    while left != len(truck_weights):

        time += 1

        if q and q[0] + bridge_length <= time:
            total -= truck_weights[left]
            left += 1
            q.popleft()

        if right < len(truck_weights) and weight >= total + truck_weights[right]:
            q.append(time)
            total += truck_weights[right]
            right += 1

    answer = time
    return answer

def main():
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    print(solution(bridge_length, weight, truck_weights))

if __name__ == "__main__":
    main()