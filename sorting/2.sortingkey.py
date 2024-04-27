# i will alwayses use sorted(listname,key) for sorting 

data =[(3,'apple'),(3,'cherry'),(3,'banana')]
data.sort(reverse=True,key=lambda x:x[1])
print(data)

#using lenght of the string 
words = ["apple", "banana", "cherry", "date", "elderberry"]
# Sort the list of strings by length
sorted_word = sorted(words,key=len)
print(sorted_word)

#Sorting a List of Tuples by Multiple Criteria
# In this example, we have a list of tuples representing people with names and ages. We will sort the list first by age in descending order and then by name in ascending order.


people = [("Alice", 30), ("Bob", 35), ("Charlie", 35), ("Alice", 28)]
# Sort the list of tuples by age (descending) and then by name (ascending)
sort_people = sorted(people,key=lambda x:(-x[1],x[0]))
print(sort_people)


# In this program, we have a list of custom objects of a class called Book. We will sort the list of books by the book's publication year in ascending order.

class Book:
    def __init__(self, name, publication, year):
        self.name = name
        self.publication = publication
        self.year = year

# Create instances of Book objects and store them in a list
books = [
    Book("Book1", "Author1", 2005),
    Book("Book2", "Author2", 1998),
    Book("Book3", "Author3", 2012),
    Book("Book4", "Author4", 2005)
]

# Sort the list of books by the 'year' attribute
sorted_by_year = sorted(books, key=lambda x: x.year)

# Print the sorted books
for book in sorted_by_year:
    print(f"The book '{book.name}' was written by {book.publication} and published in {book.year}")

    