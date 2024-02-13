class Library:
    def __init__(self):
        self.books = open("books.txt", "a+")


    def add_book(self):
        try:
            title = input("Enter the title of your book: \n").title()
            author = input("Enter the author of your book: \n").title()
            year = input("Enter the first release year of your book: \n").title()
            pages = input("Enter the number of pages of your book: \n").title()
            book_info = f"Book: {title.strip()}, Author: {author.strip()}, Release Year: {year.strip()}, Number of Pages: {pages.strip()} \n"
            self.books.write(book_info)
            print(f"\n'{title.strip()}' is successfully added to the library!\n")
        except:
            print("\nSomething went wrong, please try again!\n")
        

    def get_lines(self):
        self.books.seek(0)
        content = self.books.read()
        lines = content.splitlines()
        return lines


    def list_books(self):
        lines = self.get_lines()
        if not lines:
            print("\nThere are no books saved yet!\n")
            return None
        else:
            print("\n -----  Books  -----\n" )
            for line in lines:
                sub_line = line.split(",")
                for i in range(2):
                    print(sub_line[i], end=" |")
                print("\n")
            print("--------------------")
            print(f"There are {len(lines)} book(s) found!")
            print("--------------------\n")
            
        
    def remove_book(self):
        lines = self.get_lines()

        if not lines:
            print("\nThere are no books saved yet!\n")
        else:
            selected_book = input("\nWhich book you want to remove? \n\n").title()
            selected_book_str = f"Book: {selected_book}"
            new_lines = []
            try:
                global flag 
                flag = 0
                for line in lines:
                    if selected_book_str in line.split(","):
                        flag = 1
                    else:
                        new_lines.append(line)

                if flag == 0:
                    print(f"\n*** '{selected_book}' is not found in the list! ***\n")
                else:
                    self.books.truncate(0)

                    for line in new_lines:
                        self.books.write(line + "\n")

                    print(f"\n {selected_book} deleted successfully!\n")

            except:
                print("\nSomething went wrong, please try agin!\n")


    def __del__(self) :
        self.books.close()


while True:
    lib = Library()
    choice = input(" *** MENU ***  \n 1) List Books \n 2) Add Book \n 3) Remove Book \n q) Quit \n\n Enter your choice:")

    if choice.strip() == "1":
        lib.list_books()

    elif choice.strip() == "2":
            lib.add_book()

    elif choice.strip() == "3":
            lib.remove_book()
        
    elif choice.strip() == "q" or choice.strip() == "Q":
        exit()

    else:
        print("\n Please choose a valid option!\n")
        
    del lib
    
 



    
        
