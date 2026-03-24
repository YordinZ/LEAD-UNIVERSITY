with open("output/latin-1-output.txt", "w", encoding="latin-1") as f:
    f.write("Español")
    f.write("\n")
    f.write("Agüero")

with open("output/latin-1-output.txt", "r", encoding="latin-1") as f:
    print(f.readlines())