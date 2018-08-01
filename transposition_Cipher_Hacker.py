import pyperclip, detectEnglish, transposition_Decrypt

def main():
    myMessage = """Yteeoh yueoe  f.aa  rpm epy  l  """
    hackedMessage = hackTransposition(myMessage)
    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))
        decryptedText = transposition_Decrypt.decryptMessage(key, message)
        if detectEnglish.isEnglish(decryptedText):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()