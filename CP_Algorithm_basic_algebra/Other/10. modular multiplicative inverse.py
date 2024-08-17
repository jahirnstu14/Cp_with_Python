# A modular multiplicative inverse of an integer a  is an integer x such that a.x is congruent to 1 modular some modulus m .we want to find an integer x sothat , a.x = 1 mod m , we donote x with a^-1 , simply we can write , x = a^-1 mod m . We should note that the modular inverse does not always exist. For example, let m=4,a = 2,By checking all possible values modulo m , it should become clear that we cannot find a^-1 satisfying the above equation.

# It can be proven that the modular inverse exists if and only if a and m are relatively prime gcd(a,m) = 1

# a.x + m.y = 1, his is a Linear Diophantine equation in two variables. As shown in the linked article, when  gcd(a,m) = 1    the equation has a solution which can be found using the extended Euclidean algorithm. Note that gcd(a,m) = 1 is also the condition for the modular inverse to exist.Now, if we take modulo m of both sides, we can get rid of m.y and the equation becomes: a.x = 1 mod m , hus, the modular inverse of a is x .

# find x value form a.x + m.y = 1 which is the modular inverse of a . 

def extended_euclidean(a, m):
    if m == 0:
        return a, 1, 0
    g, x1, y1 = extended_euclidean(m, a % m)
    x = y1
    y = x1 - (a // m) * y1
    return g, x, y

def main():
    a = int(input("Enter value for a: "))
    m = int(input("Enter value for m: "))
    
    g, x, y = extended_euclidean(a, m)
    
    if g != 1:
        print("No solution!")
    else:
        x = (x % m + m) % m
        print(x)

if __name__ == "__main__":
    main()
    
# x % m might also be negative, and we first have to add m to make it positive.

# if a and m are relatively prime : a^o(m) = 1 mod m . if m is a prime , this simplifies to fermat little therorm : a^m-1 = 1 mod m . 
# multiply both side using a^-1 then we get, a^o(m)-1 = a^-1 mod m , for prime m , a^m-2 = 1 mod m .the time complexity will be o(log(n))



