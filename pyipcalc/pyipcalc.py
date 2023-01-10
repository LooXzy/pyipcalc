def convert_decimal_to_binary(nbr_decimal):
    nbr_binary = bin(nbr_decimal)[2:]

    return nbr_binary

def calc_nbr_host(cidr):
    # /1 -> /32
    cidr_rest = 32 - cidr
    nbr_host = 2**cidr_rest - 2  # 2 puissance cidr_rest

    return nbr_host

def calc_netmask_with_nbr_hote(nbr_host):
    if 1 < nbr_host < 2147483646:
        if nbr_host <= 1:
            netmask_cidr = "32"
        elif nbr_host <= 2:
            netmask_cidr = "30"
        elif nbr_host <= 6:
            netmask_cidr = "29"
        elif nbr_host <= 14:
            netmask_cidr = "28"
        elif nbr_host <= 30:
            netmask_cidr = "27"
        elif nbr_host <= 62:
            netmask_cidr = "26"
        elif nbr_host <= 126:
            netmask_cidr = "25"
        elif nbr_host <= 254:
            netmask_cidr = "24"
    else:
        netmask_cidr = "Le nombre d'hôtes demandés est incorrect"

    return  netmask_cidr

if __name__ == '__main__':
    print(calc_nbr_host(24))
    print(convert_decimal_to_binary(192))
    print(calc_netmask_with_nbr_hote(200))