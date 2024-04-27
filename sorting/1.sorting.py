
# i will always use sorted() for sorting 


number = [4,6,1,2,100]

# using sort() function
print("sorting ascending to desending order : ")
number.sort()
print(number)

print("sorting descending to asecending order ")
number.sort(reverse=True)
print(number)

# using sorted() 
print("sorting ascending to desending order : ")
new_sort = sorted(number)
print(new_sort)

print("sorting descending to asecending order ")
new_sort=sorted(number,reverse=True)
print(new_sort)


