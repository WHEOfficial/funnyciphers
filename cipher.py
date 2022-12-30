import math
import random
import re

import numpy as np

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

MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
}

permutations = [f + s for f in '.-x' for s in '.-x']

MONOALPHABETIC = []

def rotate(l, n):
    return l[n:] + l[:n]

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

def clean(text, with_space=False):
    pattern = r'[^A-Z ]' if with_space else r'[^A-Z]'
    return re.sub(pattern, '', text.upper())

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

def aristocrat(text, alphabet="RANDOM", pat=False, key=None, offset=1):
    text = text.upper()
    if pat:
        text = clean(text)
        text = " ".join([text[i:i+5] for i in range(0, len(text), 5)])

    encrpyted = ""
    normal_alphabet = LETTER_LIST.copy()
    cipher_alphabet = []
    
    if alphabet == "RANDOM":
        cipher_alphabet = LETTER_LIST.copy()
        while any([LETTER_LIST[i] == cipher_alphabet[i] for i in range(len(LETTER_LIST))]):
            random.shuffle(cipher_alphabet)
    else:
        used_letters = LETTER_LIST.copy()
        for c in key:
            if c in used_letters:
                cipher_alphabet.append(used_letters.pop(used_letters.index(c)))
        
        cipher_alphabet = rotate(cipher_alphabet + used_letters, -offset)
    
    if alphabet == "K1":
        normal_alphabet, cipher_alphabet = cipher_alphabet, normal_alphabet

    for c in text:
        o = ord(c)
        if o in LETTER_RANGE:
            encrpyted += cipher_alphabet[normal_alphabet.index(c)]
        else:
            encrpyted += c
    
    return encrpyted

def hill(text, key):
    text, key = clean(text), key.upper()
    mat_key = [ord(c) - LETTER_MIN for c in key]
    mat_key = np.reshape(mat_key, (2, 2))
    
    encrpyted = ""
    if len(text) % 2 != 0:
        text += 'Z'

    for i in range(0, len(text), 2):
        mat_text = np.reshape([ord(c) - LETTER_MIN for c in text[i:i+2]], (2, 1))
        mat_text = (np.matmul(mat_key, mat_text) % len(LETTER_LIST)).flatten()
        for c in mat_text:
            print(c)
            encrpyted += chr(c + LETTER_MIN)

    return encrpyted

def morse(text):
    text = clean(text, True)
    encrypted = ""

    for c in text:
        if c != ' ':
            encrypted += MORSE[c]
            encrypted += 'x'
        else:
            encrypted += 'x'
    
    return encrypted[:-1]

def pollux(morsept, dots=[1,2,3], dashes=[4,5,6], spaces=[7,8,9,0]):
    encrypted = ""

    morse_map = {
        '.': dots,
        '-': dashes,
        'x': spaces
    }

    for c in morsept:
        encrypted += str(random.choice(morse_map[c]))
    
    return encrypted

def morbit(morsept, perm=permutations.copy()):
    encrypted = ""

    if len(morsept) % 2 != 0:
        morsept += 'x'

    for i in range(0, len(morsept), 2):
        encrypted += str(perm.index(morsept[i:i+2]) + 1)
    
    return encrypted

#print(aristocrat("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "K1", key="COLD WEATHER", offset=2, pat=True))

random_perm = permutations.copy()
random.shuffle(random_perm)
print(morbit(morse("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")))