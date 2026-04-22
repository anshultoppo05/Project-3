from add_books import add
from issue_book import issue
from show_books import show
from return_book import return_book
from utils import print_separator

def display_menu():
    """Display the main menu"""
    print_separator("LIBRARY MANAGEMENT SYSTEM")
    print("\n1. 📚 Add New Book")
    print("2. 📖 Show All Books")
    print("3. 🔓 Issue Book to Student")
    print("4. 🔒 Return Book from Student")
    print("5. ❌ Exit")
    print_separator()

def library():
    """Main library management function"""
    while True:
        display_menu()
        
        try:
            choice = int(input("👉 Enter your choice (1-5): "))
            
            if choice == 1:
                add()
            elif choice == 2:
                show()
            elif choice == 3:
                issue()
            elif choice == 4:
                return_book()
            elif choice == 5:
                print_separator()
                print("\n👋 Thank you for using Library Management System!")
                print("   See you next time!\n".center(60))
                print_separator()
                break
            else:
                print("\n❌ Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")
            print("   Please try again.\n")

if __name__ == "__main__":
    library()
