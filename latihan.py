kata = 'BaT'
#huruf = [str(huruf) for huruf in kata]

print('kata\t= ', kata)
#print('huruf= ', huruf)


for i in range(len(kata)):
    print('\nhuruf\t= ', kata[i])
    desimal1 = ord(kata[i])
    print('desimal\t= ', desimal1)
    
    biner = ''
    oktal = ''
    hexa = ''

    #biner
    desimal=desimal1
    while desimal > 0:
        sisa = desimal % 2
        biner = str(sisa) + biner
        desimal //= 2
    print('biner\t= ', biner)

    #oktal
    desimal=desimal1
    while desimal > 0:
        sisa = desimal % 8
        oktal = str(sisa) + oktal
        desimal //= 8
    print('oktal\t= ', oktal)

    #hexa
    desimal=desimal1
    hex_chars = "0123456789ABCDEF"
    while desimal > 0:
         sisa = desimal % 16
         hexa = hex_chars[sisa] + hexa
         desimal //= 16
    print('hexa\t= ', hexa)