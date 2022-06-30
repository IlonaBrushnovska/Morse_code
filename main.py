
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '&': '.-...', "'": '.----.', '@': '.--.-.',
    ',': '--..--', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '?': '..--..', '"': '.-..-.',
    '/': '-..-.',
}

print('Welcome to Morse Code Translator!')

is_translate = True

while is_translate:
    user_text = input("Type your text to translate into Morse Code: ").upper()
    list_of_letters = [letter for letter in user_text.replace(" ", "")]
    try:
        morse_code = [morse_dict[char] for char in list_of_letters]
        translated_text = ''
        for item in morse_code:
            translated_text += f" {item}"
        print(f"Your code is '{translated_text}'")
    except:
        print("You used unexpected character. Please try again!")
    is_continue = input("Do you want to continue translating? Type 'YES' or 'NO': ").upper()

    if is_continue == 'NO':
        is_translate = False
