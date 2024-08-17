# problem link : https://leetcode.com/problems/integer-to-english-words/submissions/

LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
THOUSANDS = ["", "Thousand", "Million", "Billion"]

def number_to_words(num: int) -> str:
    if num == 0:
        return "Zero"
    
    i = 0
    words = ""
    
    while num > 0:
        if num % 1000 != 0:
            words = helper(num % 1000) + THOUSANDS[i] + " " + words
        num //= 1000
        i += 1
    
    return words.strip()

def helper(num: int) -> str:
    if num == 0:
        return ""
    elif num < 20:
        return LESS_THAN_20[num] + " "
    elif num < 100:
        return TENS[num // 10] + " " + helper(num % 10)
    else:
        return LESS_THAN_20[num // 100] + " Hundred " + helper(num % 100)

# Example usage
print(number_to_words(12345))  # Output: "Twelve Thousand Three Hundred Forty Five"
