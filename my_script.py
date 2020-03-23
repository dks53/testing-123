# testing-123/my_script.py

def enlarge(i):
    return i * 100

# need to remove from the global scope in order to import other things from this script
#my_number = input(float(("Please input a number: "))
#n = enlarge(8)
#n = enlarge(my_number)
#print("Enlarging the number ", n)

# "if this script is run from the command-line, then ..."
if __name__ == "__main__":
    original_number = int(input("Please select a number to be enlarged (e.g. 400): "))
    print("You chose:", original_number)

    bigger_number = enlarge(original_number)
    print("Enlarged number is:", bigger_number)