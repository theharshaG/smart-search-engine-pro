import os

FOLDER = "files"

def read_files():
    for filename in os.listdir(FOLDER):
        if filename.endswith(".txt"):
            path = os.path.join(FOLDER, filename)

            with open(path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, start=1):
                    yield filename, i, line.strip()

def highlight_line(line, keywords):
    words = line.split()

    new_words = []

    for word in words:
        temp = word
        for key in keywords:
            if key.lower() in word.lower():
                temp = f">>>{word}<<<"
        new_words.append(temp)

    return " ".join(new_words)

def search_keywords():
    query = input("Enter keywords (space separated): ")
    keywords = query.split()

    found = False
    count = 0

    for file, line_no, line in read_files():
        for key in keywords:
            if key.lower() in line.lower():

                highlighted = highlight_line(line, keywords)

                print(f"\n📄 {file} | Line {line_no}")
                print(highlighted)

                found = True
                count += 1
                break   # avoid duplicate prints

    if not found:
        print(" No matches found")
    else:
        print(f"\n Total matches: {count}")

def main():
    while True:
        print("\n====== SMART SEARCH ENGINE PRO ======")
        print("1. Search ")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            search_keywords()

        elif choice == "2":
            break

        else:
            print(" Invalid choice")


if __name__ == "__main__":
    main()
