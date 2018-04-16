#!/usr/bin/env python
'''
Generate a favorite artist list of songs
'''


def generate_my_music(artist,csv_in = 'c:\\test\\featuresdf.csv'):
    import pandas as pd
    music = pd.read_csv(csv_in)
    music_zip = zip(music.artists,music.name)
    
    music_list = sorted([track for track in music_zip if track[0] == artist],key=lambda track_name: track_name[1])
    print(music_list)


if __name__ == '__main__':

    generate_my_music(artist="Ed Sheeran")

