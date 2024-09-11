# The hard way is to not use those, and go from scratch, 
# using only what you would be able to do with physical electrical components.

# I'll use the following two functions to simulate two types of transistor

def nmos(input_signal, output):
    # NMOS transistor pulls output to 0 (ground) if input is 1
    return 0 if input_signal == 1 else output

def pmos(input_signal, output):
    # PMOS transistor pulls output to 1 (high) if input is 0
    return 1 if input_signal == 0 else output

def NAND(a, b):
    # output is initially high
    output = 1
    
    # NMOS transistors in series. This will pull to ground if both inputs are 1
    output = nmos(a, output)
    output = nmos(b, output)

    # PMOS transistors in parallel. This will pull to high if either input is 0
    output = pmos(a, output)
    output = pmos(b, output)
    
    return output

# Using NAND gates, we can make every other logic gate.

def NOT(a):
    # there's not really much explaining here, just think about it and it explains itself
    return NAND(a, a)

def AND(a, b):
    # an AND gate is just the opposite of a NAND gate so...
    return NOT(NAND(a, b))
    # if I were strictly using NAND gates, I'd use a NAND gate which output runs into
    # both inputs of another NAND gate, but to keep it "DRY" I haven't done that.
    # NAND only would look like: NAND(NAND(a, b), NAND(a, b))

def OR(a, b):
    # this inverts both inputs and runs it through a NAND gate
    # same thing as above with "DRY" also applies
    return NAND(NOT(a), NOT(b))
    # NAND only would look like: NAND(NAND(a, a), NAND(b, b))

def NOR(a, b):
    # "DRY" again
    return NOT(OR(a, b))
    # NAND only would look like: NAND(NAND(NAND(a, a), NAND(b, b)), NAND(NAND(a, a), NAND(b, b)))
    
def XOR(a, b):
    # XOR returns 1 only if either a or b are high, but not both
    return NAND(NAND(a, NAND(a, b)), NAND(b, NAND(a, b)))


# standard python logic is used here
def main():
    gates = ["NOT", "AND", "OR", "NAND", "NOR", "XOR"]
    print("Welcome to the logic gate simulator.")
    print("The following logic gates are available: ")
    for i, gate in enumerate(gates):
        print(str(i) + ". " + gate)
    
    gate = -1
    a = "-1"
    b = "-1"
    
    while not AND(int(gate < len(gates)), int(gate >= 0)):
        gate = int(input("Select a logic gate: "))
    
    while not a in "01" or len(a) != 1:
        a = input("Enter your first input: ")
    
    if gate != 0:
        while not b in "01" or len(b) != 1:
            b = input("Enter your second input: ")
        
    a = int(a)
    b = int(b)
        
    match gate:
        case 0:
            output = NOT(a)
        case 1:
            output = AND(a, b)
        case 2:
            output = OR(a, b)
        case 3:
            output = NAND(a, b)
        case 4:
            output = NOR(a, b)
        case 6:
            output = XOR(a, b)
    print("Output: " + str(output))
            
if __name__ == "__main__":
    main()
