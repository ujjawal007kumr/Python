def longest_increasing_subsequence(num):
    n=len(num)
    if n==0:
        return []

    lengths = [1]*n

    previous = [-1]*n

    max_length_index = 0
    for i in range(1,n):
        for j in range(i):
            if num[i]>num[j] and lengths[i]<lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                previous[i] = j

    subsequence = []
    curr_index = max_length_index
    while curr_index >= 0:
        subsequence.append(num[curr_index])
        curr_index = previous[curr_index]

    subsequence.reverse()

    return subsequence

num = [3,4,-1,0,6,2,3]
result = longest_increasing_subsequence(num)
print(result)