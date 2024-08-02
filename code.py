class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.is_available else 'No'}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {[book.title for book in self.borrowed_books]}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def issue_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn and b.is_available), None)
        member = next((m for m in self.members if m.member_id == member_id), None)

        if book and member:
            book.is_available = False
            member.borrowed_books.append(book)
            self.transactions.append(f"Issued '{book.title}' to {member.name}")
            print(f"Book '{book.title}' issued to {member.name}.")
        else:
            print("Book or Member not found, or Book is not available.")

    def return_book(self, isbn, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member:
            book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
            if book:
                book.is_available = True
                member.borrowed_books.remove(book)
                self.transactions.append(f"Returned '{book.title}' from {member.name}")
                print(f"Book '{book.title}' returned by {member.name}.")
            else:
                print("Book not found in member's borrowed books.")
        else:
            print("Member not found.")

    def view_books(self):
        for book in self.books:
            print(book)

    def view_members(self):
        for member in self.members:
            print(member)

    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)


library = Library()

# AB
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "12345")
book2 = Book("1984", "George Orwell", "67890")
library.add_book(book1)
library.add_book(book2)

# AM
member1 = Member("Alice", "A001")
member2 = Member("Bob", "B002")
library.add_member(member1)
library.add_member(member2)

# I/R B
library.issue_book("12345", "A001")
library.return_book("12345", "A001")

# View
library.view_books()
library.view_members()
library.view_transactions()