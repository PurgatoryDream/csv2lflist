import csv
from os.path import basename
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def load_dataset(path):
    f = open("collection.lflist.conf", "w")
    f.write("#[" + basename(path).split('.')[0] + " Banlist]" + "\n")
    f.write("!" + basename(path).split('.')[0] + " Banlist" + "\n")
    f.write("#" + basename(path).split('.')[0] + " Banlist" + "\n")

    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            line = ""
            if row[0] == "cardname":
                continue
            if int(row[1]) < 3:
                line = str(row[2]) + " " + str(row[1]) + " --" + str(row[0]) + "\n"
            f.write(line)

    f.close()


def main():
    Tk().withdraw()
    path = askopenfilename()
    load_dataset(path)
    return 0


main()