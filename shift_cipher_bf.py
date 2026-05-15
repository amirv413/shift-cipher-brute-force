from random import randint
from pyfiglet import figlet_format
from termcolor import colored


def load_common_words(filename='common_words.txt'):
    common_words = []
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()  
            common_words.append(word)
    return common_words

def shift_cipher_enc(plain_text: str, k: int):
    cipher_text = []
    plain_text = plain_text.lower()
    for p in plain_text:
        x = letter_to_number[p] + (k % 26)
        cipher_text.append(x)
    return cipher_text

def shift_cipher_dec(cipher_text: list, k: int):
    plain_text = ""
    for c in cipher_text:
        x = (c - (k % 26)) % 26   
        plain_text += number_to_letter[x]
    return plain_text

def encrypt_sentence(plain_sentence, k):
    cipher_sentence = []
    words = plain_sentence.split()
    for w in words:
        cipher_sentence.append(shift_cipher_enc(w, k))
        cipher_sentence.append(-1)   
    cipher_sentence.pop()           
    return cipher_sentence

def decrypt_sentence(cipher_sentence, k):
    plain_sentence = ""
    for c in cipher_sentence:
        if c == -1:
            plain_sentence += " "
        else:
            plain_sentence += shift_cipher_dec(c, k)
    return plain_sentence

letter_to_number = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

number_to_letter = {v: k for k, v in letter_to_number.items()}

k = randint(0, 25)

app_name = figlet_format("Shift Cipher Brute Force",font="standard")
app_name = colored(app_name,color="yellow")
print(app_name)

sentence = input("Enter the sentence yuo want to test in english : ")

sentence = sentence.lower()

most_common_words = load_common_words()

cipher_sentence = encrypt_sentence(sentence, k)


print(f"\nOriginal sentence: {sentence}")
print(f"Encrypted with key {k}: {cipher_sentence}\n")

print("=== Brute forcing ===")
for key in range(26):
    decrypted = decrypt_sentence(cipher_sentence, key)
    words = decrypted.split()
    
   
    if all(word in most_common_words for word in words):
        print(f"\n✅ VALID SENTENCE FOUND!")
        print(f"   Key = {key}")
        print(f"   Decrypted: {decrypted}")
        break
    else:
        print(f"Key {key} -> {decrypted}  (not found ❌ )")
        
        