#주차 요금 계산

# 출차 내역이 없으면, 23:59에 출차된것
# 기본요금+((누적시간 - 기본시간)/단위시간)*단위요금
# 단위시간 나누기는 올림 처리를 한다.
# 기본시간 이하면 기본 요금
import math


def solution(fees, records):
    answer = []
    dic = {}  # 차 출차 유무
    time = {}  # 시간 누적
    for r in records:
        temp = r.replace(':', ' ')
        temp = temp.split(" ")
        if temp[3] == 'IN':
            dic[temp[2]] = True

            if not time.get(temp[2], False):
                time[temp[2]] = -(int(temp[0]) * 60 + int(temp[1]))

            else:
                time[temp[2]] -= int(temp[0]) * 60 + int(temp[1])

        else:  # out
            dic[temp[2]] = False
            time[temp[2]] = int(temp[0]) * 60 + int(temp[1]) + time[temp[2]]

    tmp = sorted(dic)

    for t in tmp:
        if dic.get(t):  # 출차 내역이 없음
            minute = 23 * 60 + 59 + time[t]

        else:
            minute = time[t]

        if minute > fees[0]:
            answer.append(fees[1] + (math.ceil((minute - fees[0]) / fees[2])) * fees[3])

        else:  # 기본시간 이하 기본요금
            answer.append(fees[1])

    return answer

def main():
    fees=[180, 5000, 10, 600]
    records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
         "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))

if __name__ == "__main__":
    main()