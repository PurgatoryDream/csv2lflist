import csv
from os.path import basename
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Loads the dataset and reads through it to create the file:
def load_dataset(path):
    f = open(basename(path).split('.')[0] + ".lflist.conf", "w")
    f.write("#[" + basename(path).split('.')[0] + " Banlist]" + "\n")
    f.write("!" + basename(path).split('.')[0] + " Banlist" + "\n")
    f.write("$whitelist\n")
    f.write("#" + basename(path).split('.')[0] + " Banlist" + "\n")

    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')

        # Set variables in case of multiple versions of the same card:
        currentId = -1
        quantity = 0
        line = ""
        for row in reader:
            if row[0] == "cardname":
                continue

            # If the last card was the same one (diff. version), accumulate quantity.
            # Only write the line if the last one read was different.
            if int(row[2]) == currentId:
                quantity = quantity + int(row[1])
            else:
                # Save current Id and Quantity to compare with previous scenarios:
                currentId = int(row[2])
                quantity = int(row[1])
                f.write(line)

            if quantity > 3:
                quantity = 3

            line = str(currentId) + " " + str(quantity) + " --" + str(row[0]) + "\n"

        # Write the last line in the end, or else the last one won't get printed.
        f.write(line)

    f.close()


def main():
    Tk().withdraw()
    path = askopenfilename()
    load_dataset(path)
    return 0


main()
