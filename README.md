# funnyciphers

This was a program that generated random ciphers to help study for the 2022-23 Science Olympiad Codebusters event. My partner and I ended up getting second place in the Varisty division. It was my first experience creating something original with Pygame.

## Instructions
You can select the options in the start menu with the arrow keys, and use enter to toggle/change them. Most of the settings are self-explanatory, but here are a few of the weird ones:

- **Pangram mode**: sets all plaintext to "the quick brown fox jumps over the lazy dog" which is useful to understand how ciphers work. 
- **Chi-Square values**: something specific to aristocrats and patristocrats that indicates how difficult the ciphertext is. Lower is easier. The scale on the Codebusters site is (0-20 = Easy, 20-30=Medium, 30-40=Medium Hard, 40-50=Difficult, >50=Extremely Difficult). I believe this program calculates the value the same way that Science Olympiad does. You can change the range of values to determine how difficult these ciphers are.

Press space to start. You'll be able to directly type your decryption and press enter to submit it.

## Installing:
1. Create a Python virtual environment in your repo (`python -m venv venv`)
2. Activate it (run the appropriate activate file in venv/bin)
3. Install the requirements (`pip install -r requirements.txt`)
4. Run `python main.py`