def play_instrument(guitar):
    return guitar.play()

class Guitar:
    def play(self):
        print("playing the guitar")

guitar = Guitar()
play_instrument(guitar)


