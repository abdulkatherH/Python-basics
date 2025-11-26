# ENUMERATE
menu = ['Pizza', 'Burger', 'Pasta', 'Fries']
print(list(enumerate(menu, start=101)))
# for numbers, item in enumerate(menu):
#     print(f"{numbers}: {item}")

#--------------------------------------------
songs = ["Song1", "Song2", "Song3"]
for index, song in enumerate(songs, start=101):
    if song == "Song3":
        print("Current Index: ", index)
#--------------------------------------------
with open("data.txt") as file:
    for line_no, line in enumerate(file, start=1):
        print(f"{line_no}: {line.strip()}")