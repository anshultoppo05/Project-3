from utils import books, get_next_book_id, print_separator

def add():
    """Add a new book to the library"""
    print_separator("ADD NEW BOOK")
    
    while True:
        book_name = input("\n📚 Enter the Book Name: ").strip().upper()
        if not book_name:
            print("❌ Book name cannot be empty. Please try again.")
            continue
        break
    
    while True:
        try:
            copies = int(input("📦 Number of Copies to Add: "))
            if copies <= 0:
                print("❌ Number of copies must be greater than 0.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")
    
    existing_book = None
    for book_id, book_info in books.items():
        if book_info["name"] == book_name:
            existing_book = book_id
            break
    
    if existing_book:
        books[existing_book]["copies"] += copies
        print(f"\n✅ Added {copies} copies to existing book!")
        print(f"   📖 {book_name} - Total Copies: {books[existing_book]['copies']}")
    else:
        book_id = get_next_book_id()
        books[book_id] = {
            "name": book_name,
            "copies": copies,
            "issued_count": 0
        }
        print(f"\n✅ Book Added Successfully!")
        print(f"   📖 {book_name} - Copies: {copies}")
    
    print_separator()
