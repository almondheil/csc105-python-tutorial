def read_file():
    # Open the file so we can read it
    with open("plaintext_data.txt", "r") as file:
        # Get all of the lines of the file in a list
        lines = file.readlines()

        for line in lines:
            print(line)
