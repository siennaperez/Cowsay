import sys
from dragon import Dragon
from ice_dragon import IceDragon
from heifer_generator import HeiferGenerator as hg

def list_cows(cows):  # shows all cow options
    cow_names = [cow.get_name() for cow in cows]
    print("Cows available:", " ".join(cow_names))

    file_cows = hg.get_file_cows()
    file_cow_names = [cow.get_name() for cow in file_cows]
    print("File cows available:", " ".join(file_cow_names))
def find_cow(name, cows):  # returns the cow with the inputted name
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None  # if there is no cow with that name, returns none

def main():  # main function
    argv = sys.argv
    cows = hg.get_cows()

    if argv[1] == '-l':  # lists the available cows when -l is used in the terminal
        list_cows(cows)

    elif argv[1] == '-n':  # function for specified cow
        if len(argv) < 4:
            print("Error")
            return
        cow_name = argv[2]  # first word after '-n' is the cows name
        message = "".join(argv[3:])  # prints the message provided after the name
        cow = find_cow(cow_name, cows)

        if cow is not None:
            print(message)
            print(cow.get_image())
        else:
            print(f"Could not find {cow_name} cow!")  # pops up if the cow does not exist

    elif argv[1] == '-f':  # nearly the same as above, but used for file cows
        if len(argv) < 4:
            print("Error")
            return
        cow_name = argv[2]
        message = "".join(argv[3:])
        cow = find_cow(cow_name, hg.get_file_cows())  # gets the cows from the get_file_cows method in hg
        if cow is not None:
            print(message)
            print(cow.get_image())
        else:
            print(f"Could not find {cow_name} cow!")

    else:
        message = " ".join(argv[1:])
        default_cow = cows[0]
        print(message)
        print(default_cow.get_image())

        if default_cow.can_breathe_fire():
            print("This dragon can breathe fire.")
        else:
            print("This dragon cannot breathe fire.")

if __name__ == "__main__":
    main()