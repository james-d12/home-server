from dotenv import load_dotenv
import os 
import re 
import json
import eyed3
import requests

load_dotenv()
DISCOG_TOKEN = str(os.getenv("TOKEN"))

def discog_api(artist, title):
    print("Querying Discog api for artist: {} with title: {}.".format(artist, title))
    url = "https://api.discogs.com/database/search?type=release&artist={}&title={}&track={}&token={}".format(artist, title, title, DISCOG_TOKEN)
    response = json.loads(requests.get(url).content)
    if not "results" in response:
        return
    result = response["results"]
    if(result):
        #print(json.dumps(result, indent=2))
        print("- Success :)")
    return result

def get_discog_metadata(artist: str, title: str):
    new_artist = artist.replace("feat.", "&").replace("Vs", "&")
    api_artist = new_artist.partition("&")[0].strip()
    api_title = title.partition("(")[0].strip().replace("Re-Up", "")
    return discog_api(api_artist, api_title)

def process_files():
    path = str(input("Enter mp3 path: "))
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            audio_file = eyed3.load(file_path)
            file = file.replace(".mp3", "").replace("–","-")

            artist, separator, title = file.partition(" - ")
            title = title.partition("_")[0]
            title = title.replace("Re-Up", "").replace("Full Length!", "")
            title = re.sub("[\(\[].*?[\)\]]", "", title)

            if(not artist.isupper()):
                arist = artist.title()

            get_discog_metadata(artist, title)

            if audio_file.tag.artist == None or audio_file.tag.artist != artist:
                print(f"Updating artist for {file} to be {artist}.")
                audio_file.tag.artist = artist
            if audio_file.tag.title == None or audio_file.tag.title != title:
                print(f"Updating title for {file} to be {artist}.")
                audio_file.tag.title = title
            #audio_file.tag.save()

process_files()