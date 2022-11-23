"""
The problem is to maximize the score of points from taking k cards either from the left side or the right
side of the row of cards .
how to solve.
1. take the first k elements as the initial window sum and assign this sum as our current max sum
2. then start from k - 1 and decrease the current sum by the frist k element and increase the sum by
the first k element from the end
[11,49,100,20,86,29,72] k =4
score = 11 + 49 + 100 + 20 = 180
curs = 180 - 20 + 72 = 232
j = 2

"""


def cardPoints(cardpoints, k):
    score = 0
    n = len(cardpoints)
    for i in range(k):
        score += cardpoints[i]
    curr_score = score
    for j in range(k - 1, -1, -1):
        curr_score -= cardpoints[j]
        curr_score += cardpoints[n - k + j]
        score = max(score,curr_score)
    return score

print(cardPoints([11,49,100,20,86,29,72], 4))
