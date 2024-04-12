#Jose's encoder/main

def encoder(num):
    num = list(num)
    encoded_list=[]
    for item in num:
        if item == "9":
            encoded_list.append("2")
        elif item == "8":
            encoded_list.append("1")
        elif item == "7":
            encoded_list.append("0")
        else:
            encoded_list.append(str(int(item)+3))
    return "".join(encoded_list)

def decoder(num):
    num = list(num)
    decoded_list = []
    for i in num:
        if i == "0":
            decoded_list.append("7")
        elif i == "1":
            decoded_list.append("8")
        elif i == "2":
            decoded_list.append("9")
        else:
            decoded_list.append(str(int(i)-3))
    return "".join(decoded_list)


if __name__ == '__main__':
    encoded = ""
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            print(f"The encoded password is {encoded}, and the original password is {decoder(encoded)}.")
        elif option =="3":
            break

