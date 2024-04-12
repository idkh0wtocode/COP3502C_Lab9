
# Christian
def encode(password):
    pw_encoded = ""
    for digit in password:
        if int(digit) < 7:
            new_dig = int(digit) + 3
            pw_encoded += str(new_dig)
        elif int(digit) > 6:
            new_dig = (int(digit) + 3) % 10
            pw_encoded += str(new_dig)
    return pw_encoded

# Jaden
def decoder(password):
    decoder = ""
    decoder += str(password)
    decoded_password = ""
    for i in range(len(decoder)):
        decrement = int(decoder[i]) - 3
        if decrement < 0:
            decoded_password += str(10 + decrement)
            continue
        decoded_password += str(decrement)
    return decoded_password
def main():
    pw_encoded = 0
    pw = ""
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        user_input = input("Please enter an option: ")
        if user_input == "1":
            pw = input("Please enter your password to encode: ")
            pw_encoded = encode(pw)
            print("Your password has been encoded and stored!")
        elif user_input == "2":
            print(f"The encoded password is {pw_encoded}, and the original password is {decoder(pw_encoded)}")
        elif user_input == "3":
            quit()


if __name__ == '__main__':
    main()
