import itertools, os

clear = lambda: os.system("cls")

unicode_map = {
    "a": "а", "c": "с", "d": "ԁ", "e": "е", "i": "і",
    "j": "ј", "o": "ο", "p": "р", "q": "ԛ", "s": "ѕ",
    "w": "ԝ", "x": "х", "y": "у", "A": "Α", "B": "Β",
    "C": "С", "E": "Ε", "H": "Η", "I": "Ι", "J": "Ј",
    "K": "Κ", "M": "Μ", "N": "Ν", "O": "Ο", "P": "Ρ",
    "S": "Ѕ", "T": "Τ", "X": "Χ", "Y": "Υ", "Z": "Ζ"
}


#=================================================================================================================
#Ignore the mess here, I"ll write a package to do all this stuff eventually but for now enjoy the mess in the code
#=================================================================================================================

C0 = "\033[38;2;255;255;255m"
C1 = "\033[38;2;214;90;66m"

BXX = "\033[48;2;12;12;12m  "
B00 = "\033[48;2;49;49;49m  "
B01 = "\033[48;2;189;189;189m  "
B02 = "\033[48;2;255;255;255m  "
B03 = "\033[48;2;82;82;82m  "
B04 = "\033[48;2;173;66;58m  "
B05 = "\033[48;2;115;115;99m  "
B06 = "\033[48;2;90;197;189m  "
B07 = "\033[48;2;214;90;66m  "
B08 = "\033[48;2;66;156;140m  "
B09 = "\033[48;2;255;132;99m  "

banner = f"""
   {BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B00}{BXX}{BXX}{BXX}{B00}{B00}{B01}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B02}{B02}{B00}{B00}{B00}{B01}{B01}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{B00}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B02}{B02}{B02}{B02}{B01}{B01}{B01}{B01}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{B00}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B02}{B02}{B02}{B02}{B00}{B01}{B01}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{B00}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B02}{B02}{B02}{B02}{B00}{BXX}{B00}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{BXX}
   {BXX}{BXX}{B00}{B03}{B03}{B00}{BXX}{BXX}{BXX}{B00}{B00}{B02}{B02}{B02}{B02}{B02}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{BXX}{B00}{B00}{BXX}{C0}
   {BXX}{BXX}{BXX}{B00}{B03}{B03}{B00}{BXX}{B00}{B02}{B02}{B02}{B02}{B02}{B01}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B03}{B00}{B00}{BXX}{BXX}    Unicode Mapper {C1}v{C0}1.0{C1}
   {BXX}{BXX}{BXX}{BXX}{B00}{B03}{B03}{B00}{B02}{B02}{B02}{B02}{B02}{B01}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B03}{B03}{B00}{BXX}{BXX}    ====================={C0}
   {BXX}{BXX}{BXX}{BXX}{B00}{B03}{B03}{B03}{B02}{B02}{B02}{B02}{B02}{B01}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B03}{B03}{B03}{B00}{BXX}{BXX}    Input any word, the
   {BXX}{BXX}{BXX}{B00}{B03}{B03}{B03}{B02}{B02}{B02}{B02}{B02}{B01}{B01}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B00}{B00}{BXX}{B00}{B03}{B00}{B00}{BXX}{BXX}{BXX}    program will map replica
   {BXX}{BXX}{BXX}{B00}{B03}{B03}{B03}{B02}{B02}{B02}{B02}{B02}{B03}{B01}{B01}{B04}{B00}{BXX}{BXX}{BXX}{B00}{B03}{B05}{B05}{B00}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}    unicodes onto the word
   {BXX}{BXX}{BXX}{B00}{B03}{B03}{B03}{B03}{B02}{B02}{B01}{B03}{B06}{B00}{B01}{B07}{B07}{B00}{B00}{BXX}{B00}{B05}{B05}{B05}{B05}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}    which look identical, for
   {BXX}{BXX}{BXX}{B00}{B03}{B03}{B04}{B03}{B01}{B01}{B03}{B02}{B08}{B00}{B04}{B07}{B03}{B05}{B05}{B00}{B03}{B03}{B00}{B05}{B03}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}    fake OG usernames.
   {BXX}{BXX}{BXX}{BXX}{B00}{B03}{B07}{B07}{B03}{B01}{B03}{B00}{B00}{B09}{B09}{B03}{B05}{B05}{B05}{B05}{B05}{B00}{BXX}{B00}{B00}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B04}{B04}{B00}{B00}{B03}{B03}{B03}{B09}{B07}{B03}{B05}{B05}{B05}{B05}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B03}{B09}{B00}{B00}{B00}{B00}{B07}{B04}{B07}{B03}{B03}{B05}{B05}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{B00}{B03}{B03}{B04}{B09}{B04}{B00}{B09}{B09}{B07}{B07}{B03}{B03}{B03}{B03}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{B00}{B00}{B03}{B00}{B00}{B09}{B09}{B09}{B04}{B09}{B07}{B07}{B03}{B03}{B03}{B00}{B00}{B03}{B03}{B00}{B00}{BXX}{BXX}{B00}{B00}{B00}{BXX}{BXX}{BXX}{BXX}
   {BXX}{B00}{B03}{B03}{B00}{BXX}{BXX}{B00}{B09}{B07}{B07}{B07}{B07}{B03}{B03}{B03}{B00}{BXX}{BXX}{B00}{B03}{B05}{B05}{B00}{B00}{B00}{B00}{B00}{B00}{B00}{BXX}{BXX}
   {B00}{B03}{B03}{B03}{B00}{BXX}{BXX}{BXX}{B00}{B07}{B07}{B03}{B03}{B03}{B03}{B00}{BXX}{BXX}{B00}{B00}{B05}{B05}{B00}{B00}{B00}{B00}{B00}{B00}{BXX}{BXX}{BXX}{BXX}
   {B00}{B03}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B00}{B00}{B03}{B03}{B00}{B00}{B00}{B00}{B00}{B00}{B05}{B05}{B05}{B00}{B00}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{B00}{B03}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B03}{B03}{B03}{B00}{B00}{B00}{B00}{B05}{B05}{B00}{B00}{B00}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B00}{B03}{B03}{B03}{B03}{B03}{B03}{B00}{B05}{B03}{B05}{B00}{B00}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B03}{B03}{B03}{B03}{B03}{B03}{B03}{B03}{B00}{B05}{B00}{B05}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{B03}{B00}{B03}{B03}{B03}{B03}{B03}{B00}{B03}{B00}{BXX}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{BXX}{B00}{B03}{B00}{B03}{B00}{BXX}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}
   {BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{B00}{BXX}{B00}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}{BXX}

"""

#=================================================================================================================
#Eee! Ugly code!
#=================================================================================================================

def generate_variations(word, unicode_map):
    replaceable_positions = [(i, unicode_map[char]) for i, char in enumerate(word) if char in unicode_map]
    variations = set()
    for r in range(1, len(replaceable_positions) + 1):
        for combo in itertools.combinations(replaceable_positions, r):
            new_word = list(word)
            for pos, replacement in combo:
                new_word[pos] = replacement

            variations.add("".join(new_word))

    return sorted(variations)


def print_variations(word, variations, unicode_map):
    for variation in variations:
        colored_word = ""
        for original_char, new_char in zip(word, variation):
            if original_char in unicode_map and unicode_map[original_char] == new_char:
                colored_word += C1 + new_char + C0

            else:
                colored_word += new_char

        print(f"  {C1}>{C0} " + colored_word)

def save_variations(word, variations):
    filename = f"{word}.txt"
    with open(f"users/{filename}", "w", encoding="utf-8") as f:
        for variation in variations:
            f.write(variation + "\n")

def main(word):
    variations = generate_variations(word, unicode_map)
    if len(variations) > 0:
        print_variations(word, variations, unicode_map)
        option = input(f" Save to txt{C1}? ({C0}Y{C1}/{C0}N{C1}):{C0} ").strip().lower()
        if option == "y":
            save_variations(word, variations)
            print(f" Saved {len(variations)} variations to {word}{C1}.{C0}txt")

        else:
            print(" Variations not saved")

    else:
        print(f" No variations for this word found")
        
    input(f" Press {C1}'{C0}ENTER{C1}'{C0} to return to menu")
    menu()

def menu():
    clear()
    print(banner)
    word = input(f" Input a word{C1}:{C0} ").strip()
    main(word)

if __name__ == "__main__":
    os.system(f"title Unicode Mapper")
    menu()
