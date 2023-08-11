import zipfile

zip_file = zipfile.ZipFile("super-secret-info.zip")

with open("rockyou/rockyou.txt", "r") as file:
    for line in file:
        line = line.strip()
        print("Attempting password: ", line)
        try:
            zip_file.extractall(pwd=line.encode())
            print("Password found: ", line)
            break
        except Exception as e:
            continue