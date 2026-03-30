from menu import show_menu, execute

def main():
    print("Welcome to the student management system UwU")
    execute_option = True
    while execute_option:
        show_menu()
        choose = input("Select an option (1-6): ").strip()
        execute_option = execute(choose)
    print("Thanks, bye :D")

if __name__  == "__main__":
    main()