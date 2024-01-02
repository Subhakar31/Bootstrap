class library():
    def __init__(self, list):
        self.books_list=list
        self.available_books_list=list[:]
        self.lent_books={}
    def all_books(self):
        for books in self.books_list:
            print(books)

    def available_books(self):
        for books in self.available_books_list:
            print(books)

    def barrow_books(self,name,book):
        if book not in self.books_list:
            print("Your book name is incorrect. Try Again!")
            return
        if book in self.available_books_list:
            self.lent_books.update({book:name})
            self.available_books_list.remove(book)
            print("You can take your book")
        else:
            print("Your book is already taken by someone!")

    def return_books(self,book):
        del self.lent_books[book]
        self.available_books_list.append(book)
        print("Thank You! visit again.")


lib = library(["Rich dad, poor dad", "fault in our stars", "The Alchemist", "Mahabharatha", "Ramayanam", "Bhagavat gita"])
print("Welcome to Library!")
while True:
    print("1.All Books")
    print("2.Available Books")
    print("3.Barrow Books")
    print("4.Return Books")
    print("5.quit")
    user_choice = int(input("Enter your choice : "))
    if user_choice == 1:
        lib.all_books()
    elif user_choice==2:
        lib.available_books()
    elif user_choice==3:
        name = input("Enter your name :")
        book = input("Enter the book name :")
        lib.barrow_books(name,book)
    elif user_choice==4:
        book = input("Enter the book name :")
        lib.return_books(book)
    elif user_choice==5:
        break
    else:
        print("Invalid Choice!")

