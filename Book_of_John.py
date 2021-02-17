# Word Index - Analyze the text of the book of John from the Bible and display how many times each of these words show
# up in the text - 'Father', 'God', 'Christ', 'Spirit', 'life', 'man' (case sensitive). The text file is available here
# (note: all punctuation marks, chapter and verse references have been removed to allow to analyze each word)


lookup_disc = {"Father": 0, "God": 0, "Christ": 0, "Spirit": 0, "life": 0, "man": 0}
book_text = open("book of John text.txt", "r")
book_string = book_text.read()
book_list = book_string.split()
# print(book_list)

for word in book_list:
    if lookup_disc.get(word, None) is not None:
        lookup_disc[word] += 1
"""

for key in lookup_disc:
    if key in book_list not None:
        lookup_disc[key] += 1

"""
for key, value in lookup_disc.items():
    print(key + ":\t", value)


"""
lookup_list = ["Father", "God", "Christ", "Spirit", "life", "man"]
for i in lookup_list:
    count = 0
    for k in book_list:
        if i == k:
            count += 1
    print(i + ":" + "\t", count)
"""