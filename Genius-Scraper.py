import lyricsgenius as lg
filename = open("Drake bot/data/songs.txt","w",encoding='utf8')

# token changes every now and then, get yours at https://genius.com/api-clients
token = "L_0Ch2DanLyKAD8WMW23mfcIERyvExxb2cbAoC90K5IQoJm5TebCLpV3PIeYJU7h"

genius = lg.Genius(token,
                    skip_non_songs=True,excluded_terms=["(Live)"],
                    remove_section_headers=True)

#artists = ['Drake','Kanye West','Anderson Paak', 'Tupac', 'Kendrick Lamar']
artists = ['Bas']
'''
def get_lyrics(arr,k):
    c = 0
    for name in arr:
        try:
            songs = (genius.search_artist(name, 
                                          max_songs=k,
                                          sort='popularity')).songs
            s = [song.lyrics for song in songs]
            filename.write("\n\n \n\n".join(s))
            c +=1
            print(f"Songs grabbed: {len(s)}")
        except:
            print(f"Some exception at {name}: {c}")

'''
# this is just a copy of the orig function to further my own learning
def jeromes_get_lyrics(arr, count):
    c=0
    for name in arr:
        songs = (genius.search_artist(name,
                                    max_songs=count,
                                    sort='popularity')).songs
        s = [song.lyrics for song in songs]
        filename.write("\n\n".join(s))
        c += 1
        print(f"Songs grabbed: {len(s)}")

try:
    while True:
        jeromes_get_lyrics(artists, 59)
        time.sleep(3600)
        break
except:
    pass