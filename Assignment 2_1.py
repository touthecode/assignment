# Input encrypted message:
code_str = input("What is the encrypted code you want to decode? ")
text_str = ""

for i in range(len(code_str)):
# Change "*" to "a"
    if code_str[i] == "*":
        text_str += "a"
# Change "&" to "w"
    elif code_str[i] == "&":
        text_str += "e"
# Change "#" to "i"
    elif code_str[i] == "#":
        text_str += "i"
# Change "+" to "o"
    elif code_str[i] == "+":
        text_str += "o"
# Change "!" to "u"
    elif code_str[i] == "!":
        text_str += "u"
    else:
        text_str += code_str[i]
# print decoded plain text 
print(text_str)