
# https://www.hackerrank.com/challenges/c-tutorial-strings/problem

s1 = input()
s2=input()
print(f"{len(s1)} {len(s2)}")
s3=''
s3=s3+s1+s2
print(s3)
new_s1 = s2[0]+s1[1:]
new_s2 = s1[0]+s2[1:]

print(f"{new_s1} {new_s2}")