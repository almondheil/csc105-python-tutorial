def write_to_file():
    # Open the file, but now so we can write to it
    with open("new_file.txt", "w") as outfile:
        # Similar to print, but puts text into the file
        outfile.write("What are we going to do today?\n")
        outfile.write("The same thing we try to do every day, Pinky...\n")
