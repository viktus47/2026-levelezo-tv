# ez az első konzultáció

felhasznalo_neve = 'Pali'
felhasznalo_kora = 20 # input('Hány éves vagy: ')
felhasznalo_kora *= 1
# felhasznalo_kora *= 2
jegyek = [3, 4, 5]
jegyek += [1]
hallgato = {'Név': 'Józsi', 'Kor': 50}
print('Szia', 'Dr.' + felhasznalo_neve, '!', felhasznalo_kora)
print(f'Szia Dr. {felhasznalo_neve}! Kora: {felhasznalo_kora}')
print('Szia', 'Dr.' + felhasznalo_neve, '!', felhasznalo_kora, sep = '-', end = '\n\n')

print(hallgato['Név'])
print(jegyek)

print('Név:'.ljust(50, '.'))
print('Név'.rjust( 50, '.'))
print('Név'.center( 50, '.'))