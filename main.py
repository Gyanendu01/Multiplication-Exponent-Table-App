print("\n\tWelcome to the Multiplication/Exponent Table App")

def usr_input():
    usr_name = input("\n\tEnter your username: ")
    usr_num = float(input(("\tWhat number would you like to work with: ")))
    return usr_name, usr_num

def usr_output(name,num):
    print("\n\tMultiplication Table For {}".format(num))
    print("\n")
    for i in range(1,10):
        print("\t\t\t{}*{} = {}".format(num,i,round(num*i),4))
    
    print("\n\tExponentiation Table For {}".format(num))
    print("\n")
    for i in range(1,10):
        print("\t\t\t{}**{} = {}".format(num,i,round(num**i),4))

# Main function
usr_data = usr_input()
usr_output(usr_data[0],usr_data[1])
