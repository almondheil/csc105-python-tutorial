def read_file():
    with open("plaintext_data.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            print("The feeling of " + line + " is a feeling that really exists.")
