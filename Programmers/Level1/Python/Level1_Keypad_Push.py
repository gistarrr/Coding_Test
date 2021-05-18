def solution(numbers, hand):
    answer = ''

    left_pos = {'x':1, 'y':4}
    right_pos = {'x':3, 'y':4}
    cur_pos = {'x':0, 'y':0}

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            left_pos['x'] = 1
            left_pos['y'] = i // 3 + 1
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            right_pos['x'] = 3
            right_pos['y'] = i // 3
            answer += 'R'
        else :
            cur_pos['x'] = 2

            if i == 0:
                cur_pos['y'] = 4
            else:
                cur_pos['y'] = i // 3 + 1

            left_dis = abs(left_pos['x']-cur_pos['x'])+abs(left_pos['y']-cur_pos['y'])
            right_dis = abs(right_pos['x']-cur_pos['x'])+abs(right_pos['y']-cur_pos['y'])

            if left_dis < right_dis:
                left_pos['x'] = cur_pos['x']
                left_pos['y'] = cur_pos['y']
                answer += 'L'
            elif left_dis > right_dis:
                right_pos['x'] = cur_pos['x']
                right_pos['y'] = cur_pos['y']
                answer += 'R'
            else :
                if hand == "right":
                    right_pos['x'] = cur_pos['x']
                    right_pos['y'] = cur_pos['y']
                    answer += 'R' 
                else :
                    left_pos['x'] = cur_pos['x']
                    left_pos['y'] = cur_pos['y']
                    answer += 'L'

    return answer