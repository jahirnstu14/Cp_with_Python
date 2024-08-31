# https://codeforces.com/contest/2003/problem/A

def main():
    t = int(input())
    while t:
        n = int(input())
        s = list(input())
        length = len(s)
        
        if s[0]==s[length-1]:
            print("No")
        else:
            print("Yes")
            
        
        

if __name__ == "__main__":
    main()
