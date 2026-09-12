class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def available_books(self):
        print("====Available books====")
        i = 1
        for book in self.book_list:
            print(f"{i} - {book}")
            i = i+1

    def borrow_book(self , book_borrow):
        if book_borrow in self.book_list:
            self.book_list.remove(book_borrow)
            print(f"You borrowed {book_borrow} from our library and please return it in time ")
        else:
            print(f"{book_borrow} is not available")

        
    
    def return_book(self , book_return):
        if book_return in self.book_list:
            print(f"{book_return} is already in our library")
        else:
            self.book_list.append(book_return)
            print(f"You returned {book_return} ")

library = Library(["The oddesy" , "The love" , "1969" , "The big bang" , "One piece"])
n = 0
a = -1
while (a != 0):
    print("==========Library menu==========")
    print("1. Available books")
    print("2. Borrow a books")
    print("3. Return a books")
    print("4. Exit")

    choice = int(input("Enter your choice:"))
    if choice == 1:
        library.available_books()
    elif choice == 2:
        book_borrow = input("Enter the name of the book you want to borrow :")
        library.borrow_book(book_borrow)
    elif choice ==  3:
        book_return = input("Enter the book you want to return:")
        library.return_book(book_return)
    elif choice == 4:
        print("Thanks for visiting our library ")
        break
    else:
        print("Enter valid choice")
