emoji = input(">")

word_list = emoji.split(" ")

output = ""

emoji_dictionary = {
    ":)" : "😊",
    "(:" : "😥",
}
for em in word_list:
    output += emoji_dictionary.get(em, em) + " "

print(output)