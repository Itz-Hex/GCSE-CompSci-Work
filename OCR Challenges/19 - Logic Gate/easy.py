# The easy way is to just use the built in python logic operators (not, and, or, ==, != and ect)

from time import sleep

def or_logic(a, b):
    return a or b

def and_logic(a, b):
    return a and b

def xor_logic(a, b):
    return a or b if a != b else 0

def nor_logic(a, b):
    return 1 if not (a or b) else 0

def nand_logic(a, b):
    return 1 if not (a and b) else 0

def main():
    while True:
        print("Welcome to the logic gate calculator. Press Ctrl+C to exit.")
        print("Pick your logic gate: ")
        gates = ["OR", "AND", "XOR", "NOR", "NAND"]
        for i in range(5):
            print(str(i+1) + ". " + gates[i])
        choice = int(input())
        a = int(input("A: "))
        b = int(input("B: "))
        match choice:
            case 1:
                print("Result: " + str(or_logic(a, b)))
                input("Press enter to continue...")
            case 2:
                print("Result: " + str(and_logic(a, b)))
                input("Press enter to continue...")
            case 3:
                print("Result: " + str(xor_logic(a, b)))
                input("Press enter to continue...")
            case 4:
                print("Result: " + str(nor_logic(a, b)))
                input("Press enter to continue...")
            case 5:
                print("Result: " + str(nand_logic(a, b)))
                input("Press enter to continue...")
                
if __name__ == "__main__":
    main()