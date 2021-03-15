# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    a = ''
    for i in range(len(name)):
        if i == 0 or i == 3:
            a += name[i].upper()
        else:
            a += name[i]
    return a

# Test:
print(old_macdonald('macdonald'))
print(old_macdonald('aaaaaaaaaaaaaaaaaa'))
print(old_macdonald('BBBBBBBBBBBBBBB'))


