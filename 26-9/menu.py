while True:
    print("\nSelect an Option")
    option = int(input("1. Occurrences of word\n2. Character frequency\n3. Factor\n4. Exit\n"))

    if option == 1:
        text = input("Enter a sentence: ")
        word = input("Enter the word to count: ")
        count = text.split().count(word)
        print(f"The word '{word}' occurs {count} times.")

    elif option == 2:
        text = input("Enter a string: ")
        freq = {}
        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1
        print("Character frequency:")
        for k, v in freq.items():
            print(f"{k}: {v}")

    elif option == 3:
        num = int(input("Enter a number: "))
        print(f"Factors of {num} are:")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")
        print()

    elif option == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid option! Please select 1–4.")


           
