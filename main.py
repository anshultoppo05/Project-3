from add_books import add
from issue_book import issue
from show_books import show
from return_book import return_book
from utils import print_separator, get_book_statistics, get_overdue_books, search_book_by_name, get_student_borrowed_books

def display_menu():
    """Display the main menu"""
    print_separator("LIBRARY MANAGEMENT SYSTEM")
    print("\n1. 📚 Add New Book")
    print("2. 📖 Show All Books")
    print("3. 🔓 Issue Book to Student")
    print("4. 🔒 Return Book from Student")
    print("5. 📊 View Library Statistics (Dictionary-based)")
    print("6. 🔍 Search Book by Name")
    print("7. ⏰ Show Overdue Books")
    print("8. 👤 Show Books Borrowed by Student")
    print("9. ❌ Exit")
    print_separator()

def show_library_stats():
    """Display library statistics using dictionary operations"""
    print_separator("LIBRARY STATISTICS")
    stats = get_book_statistics()
    
    if stats["total_books"] == 0:
        print("\n⚠️  No books in the library yet.")
    else:
        print("\n📊 STATISTICS (from dictionary operations):")
        print(f"  • Total Book Types: {stats['total_books']}")
        print(f"  • Total Copies Available: {stats['total_copies']}")
        print(f"  • Total Copies Issued: {stats['total_issued']}")
        print(f"  • Total Copies in Stock: {stats['total_available']}")
    
    print_separator()

def search_book():
    """Search for a book in the dictionary"""
    print_separator("SEARCH BOOK")
    book_name = input("\n📚 Enter Book Name to Search: ").strip().upper()
    
    result = search_book_by_name(book_name)
    
    if result:
        print("\n✅ BOOK FOUND!")
        for book_id, book_info in result.items():
            print(f"\n  Book ID: {book_id}")
            print(f"  Name: {book_info['name']}")
            print(f"  Total Copies: {book_info['copies']}")
            print(f"  Issued Copies: {book_info['issued_count']}")
            print(f"  Available Copies: {book_info['copies'] - book_info['issued_count']}")
    else:
        print(f"\n❌ Book '{book_name}' not found in the library.")
    
    print_separator()

def show_overdue():
    """Display overdue books from the dictionary"""
    print_separator("OVERDUE BOOKS")
    
    overdue = get_overdue_books()
    
    if not overdue:
        print("\n✅ No overdue books at the moment!")
    else:
        print(f"\n⚠️  {len(overdue)} OVERDUE BOOK(S) FOUND:\n")
        print("{:<20} {:<30} {:<12} {:<10}".format("STUDENT", "BOOK NAME", "DUE DATE", "STATUS"))
        print("-" * 72)
        
        for key, record in overdue.items():
            print("{:<20} {:<30} {:<12} {:<10}".format(
                record["student_name"][:18],
                record["book_name"][:28],
                record["due_date"],
                record["status"]
            ))
    
    print_separator()

def show_student_books():
    """Show books borrowed by a specific student from dictionary"""
    print_separator("STUDENT'S BORROWED BOOKS")
    
    student_name = input("\n👤 Enter Student Name: ").strip().upper()
    student_books = get_student_borrowed_books(student_name)
    
    if not student_books:
        print(f"\n⚠️  Student '{student_name}' has not borrowed any books.")
    else:
        print(f"\n📚 BOOKS BORROWED BY {student_name}:\n")
        print("{:<30} {:<15} {:<15}".format("BOOK NAME", "ISSUE DATE", "DUE DATE"))
        print("-" * 60)
        
        for key, record in student_books.items():
            print("{:<30} {:<15} {:<15}".format(
                record["book_name"][:28],
                record["issue_date"],
                record["due_date"]
            ))
    
    print_separator()

def library():
    """Main library management function"""
    while True:
        display_menu()
        
        try:
            choice = int(input("👉 Enter your choice (1-9): "))
            
            if choice == 1:
                add()
            elif choice == 2:
                show()
            elif choice == 3:
                issue()
            elif choice == 4:
                return_book()
            elif choice == 5:
                show_library_stats()
            elif choice == 6:
                search_book()
            elif choice == 7:
                show_overdue()
            elif choice == 8:
                show_student_books()
            elif choice == 9:
                print_separator()
                print("\n👋 Thank you for using Library Management System!")
                print("   See you next time!\n".center(60))
                print_separator()
                break
            else:
                print("\n❌ Invalid choice! Please enter a number between 1 and 9.")
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")
            print("   Please try again.\n")

if __name__ == "__main__":
    library()
