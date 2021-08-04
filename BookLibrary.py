# This is a Project to make a library from where student can borrow the books they needed. 
class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print("*" ,book)
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book either not availabe or issued to someone else. Please wait until the book is availbe") 
            return False  
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you enjoyed this book")
        
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow:")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return:")
        return self.book

if __name__ == "__main__" :
    centralLibrary = Library(["Algorithms", "Django", "Python Notes", "Clrs"])
    student = Student()
    while(True):
        welcmMsg= ''''
        ****WELCOME TO CENTRAL LIBRARY****
        Please choose an option:
        1. Listing all the books
        2. Requesting a book
        3. Add or Returning a book
        4. Exit the Library
        '''
        print(welcmMsg)
        a = input("Enter a choice:")
        try:
            a = int(a)
        except Exception as e:
            print(f"Your input resulted in an error:{e}")
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing central Library! Have a great day")
            exit()
        else:
            print("Invalid input")
        
            
        
