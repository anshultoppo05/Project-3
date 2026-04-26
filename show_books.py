from utils import books, issued_books, print_separator

def show():
    """Display all books in the library with their status"""
    print_separator("AVAILABLE BOOKS IN LIBRARY")
    
    if not books:
        print("\n⚠️  No books in the library yet.")
        print_separator()
        return
    
    print("\n{:<5} {:<35} {:<12} {:<10}".format("ID", "BOOK NAME", "AVAILABLE", "ISSUED"))
    print("-" * 62)
    
    for book_id, book_info in sorted(books.items()):
        available = book_info["copies"] - book_info["issued_count"]
        issued = book_info["issued_count"]
        print("{:<5} {:<35} {:<12} {:<10}".format(
            book_id,
            book_info["name"][:33],
            available,
            issued
        ))
    
    print_separator()
    
    if issued_books:
        print("\n" + "="*60)
        print("  CURRENTLY ISSUED BOOKS".center(60))
        print("="*60)
        print("\n{:<20} {:<20} {:<15}".format("STUDENT", "BOOK NAME", "ISSUE DATE"))
        print("-" * 55)
        
        for record_key, record in issued_books.items():
            if record["status"] == "ISSUED":
                print("{:<20} {:<20} {:<15}".format(
                    record["student_name"][:18],
                    record["book_name"][:18],
                    record["issue_date"]
                ))
        
        print_separator()
