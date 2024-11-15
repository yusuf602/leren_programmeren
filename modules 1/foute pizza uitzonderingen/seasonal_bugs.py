print('Welk seizoen vind jij het fijnst?', 
      "A) Lente", 
      "B) Zomer", 
      "C) Herfst", 
      "D) Winter")
keuze = input('? ')

weer_type = ''
if keuze in ('a' or 'c'):
    print('Dus jij vindt een tussenseizoen het fijnst...')
elif keuze == 'b':
    weer_type = 'warm'
elif keuze == 'd':
    weer_type = 'koud'
else:
  print ('dat is geen optie')

if len(weer_type) > 0:
    print(f'Dus jij houd van {weer_type} weer!')