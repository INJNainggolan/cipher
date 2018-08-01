import random, sys, transposition_Encrypt, transposition_Decrypt


def main():
    random.seed(42)
    for i in range(20):
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print("Test #%s : %s..." % (i + 1, message[:50]))

        for key in range(1, len(message)):
            if message != transposition_Decrypt.decryptMessage\
                        (key, transposition_Encrypt.encryptMessage(key, message)):
                print("Mismatch with key %s and message %s" % (key, message))
                sys.exit()
    print("Transposition cipher test passed.")


if __name__ == "__main__":
    main()