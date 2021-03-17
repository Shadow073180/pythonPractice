

def read_file_and_number_every_line(filename):
    try:
        with open(filename, "r") as reader:
            lines = reader.readlines()
            counter = 1
            for line in  lines:
                print(f"{counter},{line}")
                counter += 1
        reader.close()
    except:
        print("Exception has occured")


def what_happens_when_file_doesnt_exist(filename):
    try:
        with open(filename, "r") as reader:
            lines = reader.readlines()
            counter = 1
            for line in  lines:
                print(f"{counter},{line}")
                counter += 1
        reader.close()
    except:
        print("Exception has occured\n")