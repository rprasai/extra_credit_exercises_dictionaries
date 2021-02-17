# Word Index - Analyze the text of the book of John from the Bible and display how many times each of these words show
# up in the text - 'Father', 'God', 'Christ', 'Spirit', 'life', 'man' (case sensitive). The text file is available here
# (note: all punctuation marks, chapter and verse references have been removed to allow to analyze each word)

lookup_list = ["Father", "God", "Christ", "Spirit", "life", "man"]
book_text = open("book of John text.txt", "r")
book_string = book_text.read()
book_list = book_string.split()
# print(book_list)

count = 0

for i in lookup_list:
    for k in book_list:
        if k == i:
            count += 1
    print(i + ":" + "\t", count)
