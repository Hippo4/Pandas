import pandas as pd
music = [
    ['whiterosemoxie', 'trix'],
    ['Kanye West', 'Praise God'],
    ['Jay-Z', 'Encore'],
    ['Linkin Park', 'Numb'],
    ['Soulja Boy', 'Report Card']
    ]

entries = ['artist', 'track']
playlist = pd.DataFrame(data=music, columns=entries)
print(playlist)
