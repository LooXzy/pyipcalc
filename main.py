import pyipcalc as pyip

cidr = int(input("Calcul du nombre d'hôtes, donner le masque en CIDR"))
pyip.pyipcalc.calc_nbr_hote(cidr)