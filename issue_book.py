from datetime import datetime, timedelta
from utils import books, issued_books, print_separator

def issue():
    """Issue a book to a student with tracking information"""
    print_separator("ISSUE BOOK")
    available_books = {bid: book for bid, book in books.items() if book["copies"] - book["issued_count"] > 0}
    
    if not available_books:
        print("\n❌ No books available for issuing at the moment.")
        print_separator()
        return
    
    print("\n📚 AVAILABLE BOOKS:")
    print("{:<5} {:<40} {:<10}".format("ID", "BOOK NAME", "AVAILABLE"))
    print("-" * 55)
    for book_id, book_info in sorted(available_books.items()):
        available = book_info["copies"] - book_info["issued_count"]
        print("{:<5} {:<40} {:<10}".format(book_id, book_info["name"][:38], available))
    
    print()
    while True:
        try:
            book_id = int(input("📖 Enter Book ID to Issue: "))
            if book_id not in available_books:
                print("❌ Invalid Book ID or book not available. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")
    
    book_name = books[book_id]["name"]
    
    while True:
        student_name = input("👤 Enter Student Name: ").strip().upper()
        if not student_name:
            print("❌ Student name cannot be empty. Please try again.")
            continue
        break

    while True:
        try:
            days_issued = int(input("📅 Number of Days to Issue For (recommended: 7): "))
            if days_issued <= 0:
                print("❌ Number of days must be greater than 0.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")
    issue_date = datetime.now().strftime("%Y-%m-%d")
    due_date = (datetime.now() + timedelta(days=days_issued)).strftime("%Y-%m-%d")

    record_key = f"{book_name}_{student_name}_{issue_date}"
    issued_books[record_key] = {
        "book_id": book_id,
        "book_name": book_name,
        "student_name": student_name,
        "issue_date": issue_date,
        "due_date": due_date,
        "days_issued": days_issued,
        "return_date": None,
        "status": "ISSUED"
    }
    
    books[book_id]["issued_count"] += 1
    
    print("\n" + "="*60)
    print("✅ BOOK ISSUED SUCCESSFULLY!".center(60))
    print("="*60)
    print(f"\n📚 Book: {book_name}")
    print(f"👤 Student: {student_name}")
    print(f"📅 Issue Date: {issue_date}")
    print(f"🔔 Due Date: {due_date} ({days_issued} days)")
    
    print("\n" + "-"*60)
    print("⚠️  LATE FINE NOTICE:".center(60))
    print("-"*60)
    print("\nIf the book is not returned by the due date, the following")
    print("charges will be applied per day (escalating per week):\n")
    print("  Week 1 (Days 1-7):   ₹10 per day per book")
    print("  Week 2 (Days 8-14):  ₹20 per day per book")
    print("  Week 3 (Days 15-21): ₹30 per day per book")
    print("  Week 4 (Days 22-28): ₹40 per day per book")
    print("  And so on...\n")
    print("="*60)
    print_separator()
