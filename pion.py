from pion_class import Meson
pion = Meson()
pion.display_info()
print(pion.decay())

n=int(input("Введите число распадов: "))
pions = [Meson() for _ in range (n)]
for mode,number_decays in pion.decays(pions).items():
     print(mode,':',number_decays)
