message = "this is my secret message"
#message = "WKLV LV PB VHFUHW PHVVDJH"
key = 3

mode = "encrypt"
#mode = "decrypt"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + symbol

print(translated)