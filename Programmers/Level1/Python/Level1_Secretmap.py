def solution(n, arr1, arr2):
    answer = []

    for i,j in zip(arr1, arr2):
        map_string = ""
        fir_map = format(i,'b').zfill(n)
        snd_map = format(j,'b').zfill(n)
        for k in range(n):
            if fir_map[k] == '1' or snd_map[k] == '1':
                map_string+="#"
            else :
                map_string+=" "
        answer.append(map_string)    
    return answer