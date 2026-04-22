from datetime import datetime, timedelta

# Data storage using dictionaries for better management
# books: Dictionary with book_id as key and book details as value
# Issued books structure: {book_id: {book_name, student_name, issue_date, days_issued, returned}}
books = {
    # Example: 1: {"name": "Python Basics", "copies": 3, "issued_count": 0}
}

issued_books = {
    # Example: "PYTHON BASICS_STUDENT1_2024-04-22": {
    #     "book_id": 1,
    #     "book_name": "PYTHON BASICS",
    #     "student_name": "STUDENT1",
    #     "issue_date": "2024-04-22",
    #     "days_issued": 7,
    #     "return_date": None,
    #     "status": "ISSUED"  # "ISSUED" or "RETURNED"
    # }
}

# Fine structure: 10 Rs/day in week 1, 20 Rs/day in week 2, 30 Rs/day in week 3, etc.
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
    """Generate next book ID"""
    if not books:
        return 1
    return max(books.keys()) + 1

def print_separator(title=""):
    """Print a formatted separator line"""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title.center(56)}")
        print(f"{'='*60}")
    else:
        print(f"{'='*60}")