# Write the text Take it easy to a file.
def write_to_file(filename,saying):
    try:
        f = open(filename, "a")
        f.write(saying)
        f.close()
    except:
        print("Exception has occured.")



        
            