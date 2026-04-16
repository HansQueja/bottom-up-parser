from helpers import tokenizer, shift_reduce

"""
Test cases are:
1. users should clean the printer
2. the user should clean the printer
3. users clean printers
4. the printer stopped
"""
def main():
    print(f"\nRepresentation and Processing - Coding Application\n")

    sentence = input("Enter sentence here: ")

    print(f"Sentence:\t{sentence}")

    tokens = tokenizer(sentence)

    print(f"Tokenized:\t{tokens}")

    print("\n================== Start Parsing... ==================")
    result = shift_reduce(tokens)

    if result == ["S"]:
        print("Sentence parsed into 'S'!\n")
    else:
        print(f"Failed, stack stalled at {result}\n")


if __name__ == "__main__":
    main()