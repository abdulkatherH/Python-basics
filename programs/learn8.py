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
# with open("data.txt") as file:
#     count = 0
#     word = 'You'
#     for line_no, line in enumerate(file, start=1):
#         print(f"{line_no}: {line.strip()}")
#         count += line.lower().split().count(word)
#     print(count)

def count_word_in_file(filename, word):
    count = 0
    word = word.lower()

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # print('line: ',line.lower().split().count(word))
            count += line.lower().split().count(word)
            print('count: ',count)
    return count


filename = "data.txt"   # replace with your file name
word = "You"

occurrences = count_word_in_file(filename, word)
print(f"The word '{word}' occurs {occurrences} times.")

