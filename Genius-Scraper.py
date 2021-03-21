import lyricsgenius as lg

# changing encoding to UTF8 because some lyrics have %EF %BB or something on them
filename = open("Drake bot/data/songs.txt","w",encoding='utf8')

# token changes every now and then, get yours at https://genius.com/api-clients
token = "your token here"

genius = lg.Genius(token,
                    skip_non_songs=True,excluded_terms=["(Live)"],
                    remove_section_headers=True)


# this is your list of artists; populate as you please
# leaving blank on purpose
artists = ['']

def get_lyrics(arr,k):
    c = 0
    for name in arr:
        try:
            songs = (genius.search_artist(name, 
                                          max_songs=k,
                                          sort='popularity')).songs
            s = [song.lyrics for song in songs]
            filename.write("\n\n".join(s))
            c +=1
            print(f"Songs grabbed: {len(s)}")
        except:
            print(f"Some exception at {name}: {c}")

# use try except here to mitigate timeout issue
try:
    while True:
        get_lyrics(artists, 59)
        time.sleep(3600)
        break
except:
    pass
