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

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()