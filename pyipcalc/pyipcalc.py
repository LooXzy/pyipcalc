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
        elif nbr_host <= 510:
            netmask_cidr = "23"
        elif nbr_host <= 1022:
            netmask_cidr = "22"
        elif nbr_host <= 2046:
            netmask_cidr = "21"
        elif nbr_host <= 4094:
            netmask_cidr = "20"
        elif nbr_host <= 8190:
            netmask_cidr = "19"
        elif nbr_host <= 16382:
            netmask_cidr = "18"
        elif nbr_host <= 32766:
            netmask_cidr = "17"
        elif nbr_host <= 65534:
            netmask_cidr = "16"
        elif nbr_host <= 131070:
            netmask_cidr = "15"
        elif nbr_host <= 262142:
            netmask_cidr = "14"
        elif nbr_host <= 524286:
            netmask_cidr = "13"
        elif nbr_host <= 1048574:
            netmask_cidr = "12"
        elif nbr_host <= 2097150:
            netmask_cidr = "11"
        elif nbr_host <= 4194302:
            netmask_cidr = "10"
        elif nbr_host <= 8388606:
            netmask_cidr = "9"
        elif nbr_host <= 16777214:
            netmask_cidr = "8"
        elif nbr_host <= 33554430:
            netmask_cidr = "7"
        elif nbr_host <= 67108862:
            netmask_cidr = "6"
        elif nbr_host <= 134217726:
            netmask_cidr = "5"
        elif nbr_host <= 268435454:
            netmask_cidr = "4"
        elif nbr_host <= 536870910:
            netmask_cidr = "3"
        elif nbr_host <= 1073741822:
            netmask_cidr = "2"
        elif nbr_host <= 2147483646:
            netmask_cidr = "1"
    else:
        netmask_cidr = "Le nombre d'hôtes demandés est incorrect"

    return  netmask_cidr

if __name__ == '__main__':
    print(calc_nbr_host(24))
    print(convert_decimal_to_binary(192))
    print(calc_netmask_with_nbr_hote(300))