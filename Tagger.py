import os 
import eyed3

path = str(input("Enter mp3 path: "))
for root, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(root, file)
        audio_file = eyed3.load(file_path)
        file = file.replace(".mp3", "").replace("–","-")
        artist, separator, title = file.partition(" - ")
        title, separator, extra = title.partition("_")
        title = title.replace("[", "").replace("]", "").title()

        if(not artist.isupper()):
            arist = artist.title()

        if audio_file.tag.artist == None or audio_file.tag.artist != artist:
            print(f"Updating artist for {file} to be {artist}.")
            audio_file.tag.artist = artist
        if audio_file.tag.title == None or audio_file.tag.title != title:
            print(f"Updating title for {file} to be {artist}.")
            audio_file.tag.title = title

        audio_file.tag.save()


        