numbottles = int(input())
numberexchange = int(input())

ans = numbottles

while numbottles >= numberexchange:
    remainder = numbottles % numberexchange
    numbottles //= numberexchange
    ans += numbottles
    numbottles += remainder
    
print( ans )


# one line : 
    
# formula = numBottles + (numBottles - 1) // (numExchange - 1)