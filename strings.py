letra = []
same = []
for i in range(10):
    letter = input(f"salitang {i + 1}: ")
    letra.append(letter)
    
while True:
    sukat = input("Enter a length: ")
    if sukat.isdigit():
     sukat = int(sukat)
     break
    else:
        print("Error: Maglagay ka ng tamang length.")
pareho = [letter for letter in letra if len(letter) >= sukat] 
for item in pareho:
    if len(item) >= sukat:
        same.append(item)
print(f"Ayos! Ang mga letra ay may sukat na at least", sukat, ":", pareho)
if pareho:
    print(f"Mga salita na nag rerequire ng required length:{pareho} ")
    same.append(pareho)
else:
    print("walang words ang kailangan ng required length.")