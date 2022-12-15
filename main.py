import random

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'casa', 'car', 'mono', 'elevator', 'python', 'java',
    'pleasure', 'young', 'festival', 'sing', 'class'
]


word_to_guess = random.choice(WORDS)
hangman = Hangman(word_to_guess)
hangman.play()
