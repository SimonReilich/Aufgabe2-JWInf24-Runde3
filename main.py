def int_from_char(character):
    return ord(character) - ord("a") + 1


file_name = input("Please provide the path of the .txt-file containing the input: ")
if file_name == "1" or file_name == "2" or file_name == "3" or file_name == "4" or file_name == "5":
    file_name = f"hopsen{file_name}.txt"
file = open(file_name)
text = "".join(e for e in str(file.readlines()).lower() if ord("a") <= ord(e) <= ord("z"))

a = 1
b = 0
i = 0

while a < len(text) and b < len(text):
    i += 1
    b += int_from_char(text[b])
    if b >= len(text):
        print(f"Bella hat nach {i} runden gewonnen!")
        break
    a += int_from_char(text[a])
    if a >= len(text):
        print(f"Amira hat nach {i} Runden gewonnen!")
        break
