
vertalingen = {
    'konijn': 'hond',
    'bos': 'strand',
    'vlieg': 'duif',
    'magie': 'technologie',
    'schilderij': 'foto'
}

verhaal = input('geef me een tekst: ')

woorden = verhaal.split()

hertaalde_woorden = [vertalingen.get(woord, woord) for woord in woorden]

hertaalde_tekst = ' '.join(hertaalde_woorden)
print('te vertalen teks')
print(verhaal)
print('')
print('vertallde tekst:')
print(hertaalde_tekst)
