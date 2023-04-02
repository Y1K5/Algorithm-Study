
def solution(word, n):
    dp = [0] * (n+1)
    if (word[0] == '0'):
        return 0
    dp[0] = dp[1] = 1

    for i in range(2, n+1) :
        cur = i-1
        if(word[cur] == '0' and (word[cur-1]<'1' or word[cur-1]>'2')) :
            return 0
        if(word[cur]!= '0') :
            dp[i] += dp[i-1]
        if(word[cur-1] == '1'or (word[cur] <= '6' and word[cur-1] == '2')) :
            dp[i] += dp[i-2]

        dp[i] %= 1000000
    answer = dp[n]
    return answer

if __name__ == "__main__" : 
    answer = 0

    text = input()
    answer = solution(text, len(text))
    print(answer)