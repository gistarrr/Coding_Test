def solution(tickets):
    answer = []
    result = []
    visited = [0]*len(tickets)

    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            if visited[i] == 0:
                visited[i] = 1
                answer.append("ICN")
                answer.append(tickets[i][1])                
                dfs(tickets, answer, visited, tickets[i][1], result)
                answer.pop()
                answer.pop()
                visited[i] = 0
    result.sort()
    result.sort(key = lambda x : len(x))
    return result[0]

def dfs(tickets, answer, visited, dest, result):
    if len(answer) == len(tickets) + 1:
        result.append(answer[:])
        return
    else :
        for i in range(len(tickets)):
            if visited[i] == 0 and tickets[i][0] == dest:
                visited[i] = 1
                answer.append(tickets[i][1])
                dfs(tickets, answer, visited, tickets[i][1], result)
                answer.pop()
                visited[i] = 0