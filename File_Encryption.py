# File Encryption - Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:
# codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}
# Using this example, the letter A would be assigned the symbol %, the letter a would be assigned the number 9, the letter
# B would be assigned the symbol @, and so forth. The program should open a specified text file, read its contents, then
# use the dictionary to write an encrypted version of the file’s contents to a second file. Each character in the second
# file should contain the code for the corresponding character in the first file. Use this text file to encrypt

work_file = open("info_security.txt", "r")
encrypeted_file = open("enrypted_info.txt", "w")
info_text = work_file.read()
info_list = info_text.split()
# print(new_file)
values = [
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


key = [
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

encr_dic = {}
i = 0
for k in key:
    encr_dic[k] = values[i]
    i += 1
# print(encr_dic)
# w = 0
for i in info_list:
    # while w < 1:
    encry_word = ""
    i = list(i)
    for char in i:
        cha = encr_dic.get(char, char)
        encry_word += cha
    encrypeted_file.write(encry_word + " ")
    # w += 1
    # print(i)
encrypeted_file.close()