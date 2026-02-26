#class book
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Buku '{self.title}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.title}' sedang tidak tersedia.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Buku '{self.title}' berhasil dikembalikan.")
        else:
            print(f"Buku '{self.title}' memang tidak sedang dipinjam.")

# Class Member
class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List BorrowTransaction

# Class Staff
class Staff:
    def __init__(self, name: str, staff_id: str):
        self.name = name
        self.staff_id = staff_id

# Class BorrowTransaction
class BorrowTransaction:
    def __init__(self, book: Book, member: Member, staff: Staff, borrow_date: str):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = borrow_date
        self.returned = False

    def borrow_book(self, book: Book, staff: Staff):
        print("\n=== Proses Peminjaman Buku ===")
        if not book.is_borrowed:
            book.borrow()
            self.member.borrowed_books.append(self)
            print(f"Peminjaman diproses oleh staff: {staff.name}")
            print(f"Anggota {self.member.name} meminjam pada tanggal {self.borrow_date}")
        else:
            print("Proses gagal. Buku sudah dipinjam oleh anggota lain.")

    def return_book(self, book: Book, staff: Staff):
        print("\n=== Proses Pengembalian Buku ===")
        if not self.returned:
            book.return_book()
            self.returned = True
            print(f"Pengembalian diproses oleh staff: {staff.name}")
        else:
            print("Buku sudah dikembalikan sebelumnya.")

# SIMULASI PROGRAM

# Membuat objek buku
book1 = Book("Python Programming", "John wick", "123")

# Membuat objek anggota
member1 = Member("Daffa", "001")
member2 = Member("Fajar", "002" )

# Membuat objek staff
staff1 = Staff("Admin Perpustakaan", "101")

# Membuat transaksi peminjaman
transaction1 = BorrowTransaction(book1, member1, staff1, "26-02-2026")

# Proses peminjaman
transaction1.borrow_book(book1, staff1)



# Proses pengembalian
transaction1.return_book(book1, staff1)

transaction2 = BorrowTransaction(book1, member2, staff1, "27-02-2026")
transaction2.borrow_book(book1, staff1)