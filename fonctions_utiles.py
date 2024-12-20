def mot_miniscule(mot):
    L = list(mot)
    mot_min = ''
    for i in range(len(L)):
        if ord(L[i]) > 62 and ord(L[i]) < 95:
            L[i] = chr(ord(L[i]) + 32)
    for i in range(len(L)):
        mot_min = mot_min + L[i]
    return mot_min
