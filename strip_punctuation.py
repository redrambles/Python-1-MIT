import string

text = 'goodbye! cruel, harsh world!..?!'

stripped = ""

for c in text:
    if c in string.punctuation:
        c = ""
    else:
        c == c

    stripped += c


print stripped
