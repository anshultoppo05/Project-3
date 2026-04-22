from datetime import datetime
from utils import books, issued_books, calculate_fine, print_separator

def return_book():
    """Return a book with fine calculation if overdue"""
    print_separator("RETURN BOOK")
    
    # Get issued books
    pending_books = {k: v for k, v in issued_books.items() if v["status"] == "ISSUED"}
    
    if not pending_books:
        print("\n⚠️  No issued books to return at the moment.")
        print_separator()
        return
    
    print("\n📚 ISSUED BOOKS PENDING RETURN:")
    print("{:<20} {:<30} {:<15}".format("STUDENT", "BOOK NAME", "DUE DATE"))
    print("-" * 65)
    
    count = 0
    for record_key, record in pending_books.items():
        count += 1
        print("{:<20} {:<30} {:<15}".format(
            record["student_name"][:18],
            record["book_name"][:28],
            record["due_date"]
        ))
    
    print()
    
    # Get student name and book name for return
    while True:
        student_name = input("👤 Enter Student Name: ").strip().upper()
        if not student_name:
            print("❌ Student name cannot be empty. Please try again.")
            continue
        break
    
    while True:
        book_name = input("📖 Enter Book Name: ").strip().upper()
        if not book_name:
            print("❌ Book name cannot be empty. Please try again.")
            continue
        break
    
    # Find the matching record
    record_key = None
    matching_record = None
    
    for key, record in pending_books.items():
        if record["student_name"] == student_name and record["book_name"] == book_name:
            record_key = key
            matching_record = record
            break
    
    if not matching_record:
        print("\n❌ No matching record found for this student and book combination.")
        print("   Please check the student name and book name.")
        print_separator()
        return
    
    # Calculate fine if overdue
    return_date = datetime.now().strftime("%Y-%m-%d")
    due_date = datetime.strptime(matching_record["due_date"], "%Y-%m-%d")
    return_date_obj = datetime.strptime(return_date, "%Y-%m-%d")
    
    days_overdue = (return_date_obj - due_date).days
    fine = 0 if days_overdue <= 0 else calculate_fine(days_overdue)
    
    # Update record
    issued_books[record_key]["return_date"] = return_date
    issued_books[record_key]["status"] = "RETURNED"
    
    # Update book availability
    book_id = matching_record["book_id"]
    books[book_id]["issued_count"] -= 1
    
    # Display return confirmation
    print("\n" + "="*60)
    if days_overdue <= 0:
        print("✅ BOOK RETURNED ON TIME!".center(60))
    else:
        print("⚠️  BOOK RETURNED LATE!".center(60))
    print("="*60)
    
    print(f"\n📚 Book: {book_name}")
    print(f"👤 Student: {student_name}")
    print(f"📅 Due Date: {matching_record['due_date']}")
    print(f"📅 Return Date: {return_date}")
    
    if days_overdue > 0:
        print(f"\n⏰ Days Overdue: {days_overdue} day(s)")
        print(f"💰 Fine Amount: ₹{fine}")
        print("\nFine Breakdown (escalating per week):")
        
        # Show fine breakdown
        remaining_days = days_overdue
        week = 1
        day_count = 0
        
        while remaining_days > 0:
            days_in_this_week = min(remaining_days, 7)
            rate_per_day = 10 * week
            week_fine = days_in_this_week * rate_per_day
            print(f"  Week {week}: {days_in_this_week} day(s) × ₹{rate_per_day}/day = ₹{week_fine}")
            remaining_days -= days_in_this_week
            week += 1
    else:
        print(f"\n✅ No fine applicable. Thank you for returning on time!")
    
    print("\n" + "="*60)
    print_separator()
