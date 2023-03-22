def encode(password):
    encoded_string = []
    for number in password:
        encoded_password = str((int(number) + 3) % 10)
        encoded_string.append(encoded_password)
    final_password = "".join(encoded_string)
    return final_password

def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menu_option = int(input("\nPlease enter an option: "))
        if menu_option == 1:
            user_input = input("Please enter your password to encode: ")
            encoded_pass = encode(user_input)
            print("Your password has been encoded and stored!\n")
        if menu_option == 2:
            print(f'The encoded password is {encoded_pass}, and the original password is {user_input}.\n')
        if menu_option == 3:
            break

if __name__ == "__main__":
    main()
