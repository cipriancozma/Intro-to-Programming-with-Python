# Alfabet NATO
# a) Codare: scrieti o functie to_nato(text) care traduce un text normal (o valoare string) la un text codat folosind alfabetul fonetic NATO: fiecare litera din text e inlocuita cu un cuvant specific (cuvintele fiind separate cu spatii). Observatie: doar literele sunt transformate, celelalte caractere (cifre, simboluri) raman asa cum sunt.

# Lista de cuvinte NATO: Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, Xray, Yankee, Zulu (mai multe detalii)
# b) Decodare: scrieti o functie from_nato(nato_encoding) care face transformare inversa, obtinand dintr-un text codat cu alfabetul NATO forma lui normala.

# Exemplu:

# text = "Wantsome! 123"
# nato_text = to_nato(text)
# print(nato_text)  # Whiskey Alfa November Tango Sierra Oscar Mike Echo ! 123
# print(from_nato(nato_text))  # wantsome!123

alfabet_nato = {
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

def to_nato(text):
    text_nou = ''
    text_upper = text.upper()
    for char in text_upper:
        if char.isalpha():
            text_nou += alfabet_nato[char] + " "
        else:
            text_nou += char
    return text_nou.strip()

def from_nato(nato_text):
    text_nou = ''
    text_to_array = nato_text.split()
    valoare_cheie = {valoare: cheie for cheie, valoare in alfabet_nato.items()}
    for elem in text_to_array:
        if elem in valoare_cheie:
            text_nou += valoare_cheie[elem]
        else:
            text_nou += elem
    return text_nou.lower()



text = "Wantsome! 123"
nato_text = to_nato(text)
print(nato_text)  # Whiskey Alfa November Tango Sierra Oscar Mike Echo ! 123
print(from_nato(nato_text))  # wantsome!123
