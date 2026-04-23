from datetime import datetime, timedelta

# ========== DATA STORAGE USING DICTIONARIES ==========
# books: Dictionary with book_id as key and book details (dict) as value
# Structure: {book_id: {"name": str, "copies": int, "issued_count": int}}

books = {
    # Example: 1: {"name": "Python Basics", "copies": 3, "issued_count": 0}
}

# issued_books: Dictionary with record_key as key and issue details (dict) as value
# Structure: {record_key: {"book_id": int, "book_name": str, "student_name": str, 
#                          "issue_date": str, "due_date": str, "return_date": str/None, 
#                          "status": str, "days_issued": int}}

issued_books = {
    # Example: "PYTHON BASICS_STUDENT1_2024-04-22": {
    #     "book_id": 1,
    #     "book_name": "PYTHON BASICS",
    #     "student_name": "STUDENT1",
    #     "issue_date": "2024-04-22",
    #     "due_date": "2024-04-29",
    #     "days_issued": 7,
    #     "return_date": None,
    #     "status": "ISSUED"  # "ISSUED" or "RETURNED"
    # }
}

# Configuration dictionary for fine rates
FINE_CONFIG = {
    "week_1": {"days": (1, 7), "rate": 10},
    "week_2": {"days": (8, 14), "rate": 20},
    "week_3": {"days": (15, 21), "rate": 30},
    "week_4": {"days": (22, 28), "rate": 40}
}

# ========== DICTIONARY UTILITY FUNCTIONS ==========

def calculate_fine(days_overdue):
    """Calculate fine based on days overdue with escalating rates per week"""
    if days_overdue <= 0:
        return 0
    
    total_fine = 0
    remaining_days = days_overdue
    week = 1
    
    while remaining_days > 0:
        days_in_this_week = min(remaining_days, 7)
        rate_per_day = 10 * week
        total_fine += days_in_this_week * rate_per_day
        remaining_days -= days_in_this_week
        week += 1
    
    return total_fine

def get_next_book_id():
    """Generate next book ID using dictionary keys"""
    if not books:
        return 1
    return max(books.keys()) + 1

def search_book_by_name(book_name):
    """Search for a book in the dictionary by name"""
    for book_id, book_info in books.items():
        if book_info["name"] == book_name:
            return {book_id: book_info}
    return {}

def get_book_statistics():
    """Get statistics from books dictionary"""
    if not books:
        return {"total_books": 0, "total_copies": 0, "total_issued": 0}
    
    stats = {
        "total_books": len(books),
        "total_copies": sum(book["copies"] for book in books.values()),
        "total_issued": sum(book["issued_count"] for book in books.values()),
        "total_available": sum(book["copies"] - book["issued_count"] for book in books.values())
    }
    return stats

def get_student_borrowed_books(student_name):
    """Get all books borrowed by a specific student from issued_books dictionary"""
    student_books = {}
    for key, record in issued_books.items():
        if record["student_name"] == student_name and record["status"] == "ISSUED":
            student_books[key] = record
    return student_books

def get_overdue_books():
    """Get all overdue books from issued_books dictionary"""
    overdue = {}
    today = datetime.now()
    for key, record in issued_books.items():
        if record["status"] == "ISSUED":
            due_date = datetime.strptime(record["due_date"], "%Y-%m-%d")
            if today > due_date:
                overdue[key] = record
    return overdue

def print_book_dictionary():
    """Display the books dictionary in a formatted way"""
    print("\n📚 BOOKS DICTIONARY STRUCTURE:")
    print("-" * 60)
    for book_id, book_info in books.items():
        print(f"Book ID: {book_id}")
        for key, value in book_info.items():
            print(f"  ├─ {key}: {value}")
        print()

def print_issued_books_dictionary():
    """Display the issued_books dictionary in a formatted way"""
    print("\n📖 ISSUED BOOKS DICTIONARY STRUCTURE:")
    print("-" * 60)
    for record_key, record_info in issued_books.items():
        print(f"Record Key: {record_key}")
        for key, value in record_info.items():
            print(f"  ├─ {key}: {value}")
        print()

def print_separator(title=""):
    """Print a formatted separator line"""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title.center(56)}")
        print(f"{'='*60}")
    else:
        print(f"{'='*60}")