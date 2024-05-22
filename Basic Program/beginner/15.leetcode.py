# https://leetcode.com/problems/student-attendance-record-i/

def checkRecord(s):
        return s.count('A')<=1 and s.count("LLL")==0
    
    
str1 =input()
str2=checkRecord(str1)

print(str2)
    