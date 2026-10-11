# Vezérlőszerkezetek

def korszamlalas (kor):
    while kor < 65:
        kor += 1
        if kor == 52:
            continue
        print(kor)
        if kor == 55:
            break

    else:
        print('Nyugger')
    print('Vége')
    return kor

# programfutás

print('Női nyugdíj: ', korszamlalas(40))
print('Nyugdíj: ', korszamlalas(56))

felhasznalo_kora = 20 # int(input('Hány éves vagy: '))
if felhasznalo_kora < 18:
    print('Gyerek')
elif felhasznalo_kora < 30:
    print('Fiatal felnőtt.')
elif felhasznalo_kora < 65:
    print('Középkorú')
else:
    print('Nyugger')


