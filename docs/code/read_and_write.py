def read_and_write():
    # Open the first file inline so we can read its data before closing it
    infile = open("plaintext_data.txt", "r")
    lines = infile.readlines()
    infile.close()

    # Open up a new file for writing using a with ... as expression
    with open("new_file.txt", "w") as outfile:
        for line in lines:
            emotion = line[:-1]
            outfile.write("The feeling of " + emotion + " is a feeling that really exists.\n")
