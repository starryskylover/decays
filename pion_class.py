import random
class Meson:
    def __init__(self):
        self.__name = 'Пион'
        self.__charge = -1

    def display_info(self):
        print("Эта частица - ", self.__name, "\nЕё заряд: ", self.__charge)

    def decay(self):
        fraction = random.random()
        if  fraction <= 0.000001230:
            return "pion -> e + nu_e or modes with fraction < 10^-8"
        elif fraction <= 0.000001230 + 0.000002:
            return "pion -> mu + nu_mu + gamma"
        elif fraction <= 0.000001230 + 0.000002+0.9998770:
            return "pion -> mu + nu_mu"
        else:
            return "uncounted"

    def decays(self, pions):
         modes = {
                            "pion -> e + nu_e or modes with fraction < 10^-8":0,
                            "pion -> mu + nu_mu + gamma":0,
                            "pion -> mu + nu_mu":0,
                            "uncounted":0
                  }
         for pion in pions:
             mode = pion.decay()
             modes[mode] = modes[mode] + 1
         return modes
