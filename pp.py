import sys
print('Paiskaa tähän nimes, jos olet Joona:')
nimi={}
for i in range(5):
    nimi[i]=input()
    if nimi[i] != 'Joona':
        i = i+1
        print('Yritä uudestaan. Ei se nimi sattunut oleen se Joona esim..??')
        salis = '0'
        continue
    print('Hei Joona. Laitahan salasana')
    salis=input()
    if salis=='1234':
        print('Well done')
        sys.exit()
        break
    
print('Ei sitten!!!')
for n in sorted(nimi.values()):
    print(n)


