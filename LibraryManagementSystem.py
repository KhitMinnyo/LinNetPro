import json

class Book:
    def __init__(self, title, author, is_available=True, borrower=None):
        self.title = title 
        self.author = author 
        self.is_available = is_available 
        self.borrower = borrower 

    def borrow_book(self, borrower_name):
        if self.is_available:
            self.is_available = False
            self.borrower = borrower_name
            print(f"Success. {borrower_name} can get '{self.title}'.")
            return True
        else:
            print(f"Sorry. '{self.title}' is already borrowed.")
            return False

    def return_book(self):
        self.is_available = True 
        self.borrower = None
        print(f"Thank you. '{self.title}' is received.")

    def show_status(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrower}"
        print(f"Book: {self.title:<20} | Author: {self.author:<15} | Status: {status}")

class Library:
    def __init__(self, filename="library_data.json"):
        self.books = []
        self.filename = filename 
        self.load_books() # to read data while running program

    def add_book(self, book_obj):
        self.books.append(book_obj)
        self.save_books() # store data after adding
        print(f"A new book '{book_obj.title}' is added.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book 
        return None 

    def save_books(self):
        # store data in JSON after converting from Object to Dictionary 
        data_to_save = []
        for book in self.books:
            data_to_save.append({
                "title": book.title,
                "author": book.author,
                "is_available": book.is_available,
                "borrower": book.borrower
            })
        
        try: 
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Save Error: {e}")

    def load_books(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as f:
                loaded_data = json.load(f)
                for item in loaded_data:
                    # using file data to recreate object
                    new_book = Book(item['title'], item['author'], item['is_available'], item['borrower'])
                    self.books.append(new_book)
        except FileNotFoundError:
            pass # for the first run, there is no books
        except json.JSONDecodeError:
            print("Error: Data file is corrupted.")

    def show_all_books(self):
        if not self.books:
            print("\nThere is no book in Library.")
        else:
            print("\n" + "="*60)
            print("--- All Books in Library ---")
            for book in self.books:
                book.show_status()
            print("="*60)

# --- Execution ---
my_library = Library()



while True:
    print("\n***** Library Management System V2.0 *****")
    print("1. Lists all books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Add new books")
    print("5. Exit")

    choice = input("Please, enter 1 to 5: ")

    if choice == "1":
        my_library.show_all_books()

    elif choice == "2":
        name = input("Enter book name to borrow: ")
        book = my_library.find_book(name)
        if book:
            user_name = input("Enter your name: ")
            if book.borrow_book(user_name):
                my_library.save_books() # Updating after borrowing
        else:
            print("Book not found.")

    elif choice == "3":
        name = input("Enter book name to return: ")
        book = my_library.find_book(name)
        if book:
            book.return_book()
            my_library.save_books() # Updating after returning
        else:
            print("This book is not ours.")

    elif choice == "4":
        title = input("Enter book title: ")
        author = input("Enter Author's name: ")
        new_book = Book(title, author)
        my_library.add_book(new_book)
    
    elif choice == "5":
        print("Thank you for using our Library. Have a nice day! Goodbye!")
        break 
    else:
        print("Please enter 1 to 5 only.")
