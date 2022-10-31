import math
import random

LETTER_MIN = 65
LETTER_MAX = 90
LETTER_RANGE = range(LETTER_MIN, LETTER_MAX + 1)
LETTER_LIST = [chr(c) for c in LETTER_RANGE]

NUMBER_MIN = 48
NUMBER_MAX = 57
NUMBER_RANGE = range(NUMBER_MIN, NUMBER_MAX + 1)

FREQUENCIES = {
    'E': 0.1249,
    'T': 0.0928,
    'A': 0.0804,
    'O': 0.0764,
    'I': 0.0757,
    'N': 0.0723,
    'S': 0.0651,
    'R': 0.0628,
    'H': 0.0505,
    'L': 0.0407,
    'D': 0.0382,
    'C': 0.0334,
    'U': 0.0273,
    'M': 0.0251,
    'F': 0.024,
    'P': 0.0214,
    'G': 0.0187,
    'W': 0.0168,
    'Y': 0.0166,
    'B': 0.0148,
    'V': 0.0105,
    'K': 0.0054,
    'X': 0.0023,
    'J': 0.0016,
    'Q': 0.0012,
    'Z': 0.0009,
}

MONOALPHABETIC = []

def chi_squared(text):
    text_freqs = {}

    chi_squared_value = 0
    length = 0

    for c in text.upper():
        if ord(c) in LETTER_RANGE:
            text_freqs[c] = text_freqs.get(c, 0) + 1
            length += 1
    
    for k, v in FREQUENCIES.items():
        actual = text_freqs.get(k, 0)
        expected = v * length
        diff = actual - expected
        chi_squared_value += (diff*diff) / expected
    
    return chi_squared_value

def count_letters(text):
    counts = {}
    for c in text:
        if ord(c) in LETTER_RANGE:
            counts[c] = counts.get(c, 0) + 1
    
    return counts

def caesar_encrypt(text, shift=3):
    text = text.upper()
    encrpyted = ""
    for c in text:
        o = ord(c)
        if o in LETTER_RANGE:
            pos = o - LETTER_MIN
            new_pos = (pos + shift) % 26
            new_c = chr(new_pos + LETTER_MIN)
            encrpyted += new_c
        else:
            encrpyted += c
    
    return encrpyted

def porta_encrypt(text, key):
    text, key = text.upper(), key.upper()
    encrpyted = ""
    i = 0
    for c in text:
        o = ord(c)
        if o in LETTER_RANGE:
            # thank you toebes for giving me nice code so i don't have to write 
            # out the alphabet manually
            text_value = o - LETTER_MIN
            key_value = ord(key[i % len(key)]) - LETTER_MIN
            cipher_value = 0
            if text_value < 13:
                cipher_value = ((math.floor(key_value / 2) + text_value) % 13) + 13
            else:
                cipher_value = (13 - math.floor(key_value / 2) + text_value) % 13
            encrpyted += chr(cipher_value + LETTER_MIN)
            i += 1
        else:
            encrpyted += c
    return encrpyted

def aristocrat(text, alphabet=None, key=None):
    text = text.upper()
    encrpyted = ""
    cipher_alphabet = LETTER_LIST.copy()
    while any([LETTER_LIST[i] == cipher_alphabet[i] for i in range(len(LETTER_LIST))]):
        random.shuffle(cipher_alphabet)

    for c in text:
        o = ord(c)
        if o in LETTER_RANGE:
            encrpyted += cipher_alphabet[o - LETTER_MIN]
        else:
            encrpyted += c
    
    return encrpyted