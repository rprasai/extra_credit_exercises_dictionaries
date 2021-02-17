work_file = open("enrypted_info.txt", "r")
new_file = work_file.read()
new_file = new_file.split()
decrypeted_file = open("decrypted_info.txt", "w")
# print(new_file)
key = [
    "}",
    "{",
    "]",
    "[",
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    "|",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "°",
    "±",
    "²",
    "³",
    "´",
    "µ",
    "¶",
    "·",
    "¸",
    "¹",
    "º",
    "»",
    "¼",
    "½",
    "¾",
    "¿",
]


values = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
print(len(values))
print(len(key))

decr_dic = {}
i = 0
for k in key:
    decr_dic[k] = values[i]
    i += 1
# print(encr_dic)
# w = 0
for i in new_file:
    # while w < 1:
    decry_word = ""
    i = list(i)
    for char in i:
        char = decr_dic.get(char, char)
        decry_word += char
    decrypeted_file.write(decry_word + " ")
    # w += 1
    # print(i)
decrypeted_file.close()