

class User:
    def __init__(self,name,id,password) -> None:
        self.name = name
        self.id = id
        self.password = password
        self.borrow_books = []
        self.returned_books = []

class Library:
    def __init__(self, book_list) -> None:
        self.book_list = book_list

    def borrow_book(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print("To borrow again, you have to return the borrowed book first.")
                    return
                if self.book_list[book] == 0:
                    print("Not available right now. TYou can borrow book few days latter")
                    return
                self.book_list[book] -= 1
                user.borrow_books.append(bookName)
                print("You have borrowed this book")
                return 
        print("Book not available")
    
    def return_book(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if book in user.borrow_books:
                    self.book_list[book] += 1
                    user.borrow_books.remove(bookName)
                    user.returned_books.append(bookName)
                    print("Book returned successfully")
                    return 
                else:
                    print("You can only return your own borrowed books")
                    return 
        print("This is not our book.")
    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0 :
                print(book, self.book_list[book])

    def donate(self,bookName,amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print("Thanks for donation")
                return
        self.book_list[bookName] = amount
        print("Thanks for donation")


library = Library({"English":1,"Bangla":5,"Math":3})
allUsers = [] 
currentUser = None

while True:
    if currentUser == None:
        print("Not logged in\nPlease Login or create account (L/C)")
        option = input("L/C:")
        if option == "L":
            id = int(input("id: "))
            password = input("Password: ")
            match = False 
            for user in allUsers:
                if user.id == id and user.password == password:
                    currentUser = user 
                    match = True 
            if match == False:
                print("Invalid username or password")
        else:
            name = input("Name: ")
            id = int(input("Id: "))
            password = input("Password: ")
            found = False
            for user in allUsers:
                if user.id == id:
                    print("There already an account with this id")
                    found = True
            if found:
                print("There already an account with this id")
                continue;
            user = User(name,id,password)
            currentUser = user 
            allUsers.append(user)   
    else:
        print("OPTIONS")
        print("_______")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Borrowed books list")
        print("4. Returned books list")
        print("5. Check availability")
        print("6. Donate")
        print("7. Logout")
        x = int(input("Give option: "))
        if x==1:
            bookName=input("Book name: ")
            library.borrow_book(bookName,currentUser)
        elif x==2:
            bookName=input("Book name: ")
            library.return_book(bookName,currentUser)
        elif x==3:
            print(currentUser.borrow_books)
        elif x==4:
            print(currentUser.returned_books)
        elif x==5:
            library.availability()
        elif x==6:
            bookName = input("Book name: ")
            amount = int(input("Amount: "))
            library.donate(bookName,amount)
        elif x==7:
            currentUser=None 
        print("\n\n")  