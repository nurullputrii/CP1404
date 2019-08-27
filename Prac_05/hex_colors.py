"""
CP1404 Programming 2\
Color names in dictionaries\
"""

COLOR_NAMES = {
    'AliceBlue': '#f0f8ff',
    'BlueViolet': '#8a2be2',
    'BlanchedAlmond' : '#ffebcd',
    'CadetBlue': '#5f9ea0',
    'chocolate': '#d2691e',
    'coral': '#ff7f50',
    'CornflowerBlue': '#6495ed',
    'DarkOliveGreen': '#556b2f',
    'DarkOrange': '#ff8c00',
    'DarkOrchid': '#9932cc'
}

color = str(input('Enter the color: '))
while color != "":
    if color in COLOR_NAMES:
        print(color, "is ", COLOR_NAMES[color])
    else:
        print('invalid input')
    color = str(input('Enter the color: '))