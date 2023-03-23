def encode(password):
    # Mina Alkhazraji
    encoded_string = []
    for number in password:
        encoded_password = str((int(number) + 3) % 10)
        encoded_string.append(encoded_password)
    final_password = "".join(encoded_string)
    return final_password

def decode(password):
    # written by Nikhil Mishra
    decoded_pass = ""
    for num in password:
        decoded_pass += (str(abs((int(num) - 3) % 10)))
    return decoded_pass

def main():
    encoded_pass = ""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menu_option = int(input("\nPlease enter an option: "))
        if menu_option == 1:
            user_input = input("Please enter your password to encode: ")
            encoded_pass = encode(user_input)
            print("Your password has been encoded and stored!\n")
        if menu_option == 2:
            print(f'The encoded password is {encoded_pass}, and the decoded password is {decode(encoded_pass)}.\n')
        if menu_option == 3:
            break

if __name__ == "__main__":
    main()
