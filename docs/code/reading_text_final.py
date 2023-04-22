def read_file():
    with open("plaintext_data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            emotion = line[:-1]
            print("The feeling of " + emotion + " is a feeling that really exists.")
