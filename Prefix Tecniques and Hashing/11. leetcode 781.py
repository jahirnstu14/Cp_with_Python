

# The approach is simple if one 🐇 rabbit answers 10 then at most 11 🐇 rabbits can answer 10 and they have the same color.
# For example:- Answer = [1,1,2,2,2,2,2]
# 2 rabbits answer 1 so it is possible that at most 2 rabbits can answer 1.
# [1,1] count = 2(2: answered, 0:Not Answered)

# 5 rabbits answer 2 so it is possible that at most 3 rabbits can answer 2.
# [2,2,2] count = 3 (3: answered, 0:Not Answered)

# and the remaining 2 rabbits can be of the same color.
# [2,2] count = 3(2: answered, 1:Not Answered)

# Numbers of Rabbits = 2+3+3 = 8

# Complexity
# Time complexity:O(N)
# Space complexity:O(N)

answers = list(map(int,input().split()))

if answers is None or len(answers)<1:
    print(0)
    
mp = [0]*1000
answer = 0

for i in answers:
    mp[i]+=1
    if mp[i]==1:
        answer+=i+1
    
    if mp[i]==i+1:
        mp[i]=0

print(answer)
        