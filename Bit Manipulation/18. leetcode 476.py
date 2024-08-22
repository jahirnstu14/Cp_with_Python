# complement of a number 

class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

# Example with num = 5
solution = Solution()
num = 5
result = solution.findComplement(num)
print("Complement of", num, "is", result)


# another way without bit operation 

class Solution:
    def findComplement(self, num):
        # Convert number to binary representation stored in a list
        temp = []
        while num != 0:
            temp.append(num % 2)
            num //= 2
        
        # Make the complement
        for i in range(len(temp)):
            if temp[i] == 1:
                temp[i] = 0
            else:
                temp[i] = 1
        
        # Convert binary back to decimal
        res = 0
        for i in range(len(temp)-1, -1, -1):
            res = res * 2 + temp[i]
        
        return res

# Example usage
solution = Solution()
num = 5
result = solution.findComplement(num)
print("Complement of", num, "is", result)
