import requests

class Music:
    def __init__(self, song_name, artist_name, album_name, music_link):
        self.song_name = song_name
        self.artist_name = artist_name
        self.album_name = album_name
        self.music_link = music_link

    def __str__(self) -> str:
        #name = ", ".join(self.artist_name)
        return f"{self.song_name} by {self.artist_name}\n album: {self.album_name}\n music:{self.music_link}"
    
class MusicFetcher:
    def __init__(self, track_name):
        self.track_name = track_name
        self.url = f"https://itunes.apple.com/search?term={track_name}&media=music"
    
    def request_music_api(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        return []
    
    @staticmethod
    def read_data(music):
        song_name = music.get("trackName", "Unknown")
        artist_name = music.get("artistName", "Unknown")
        album_name = music.get("collectionName", "Unknown")
        music_link = music.get("trackViewUrl", "No link available")
        return song_name, artist_name, album_name, music_link
    
    def display_music_results(self):
        data = self.request_music_api()
        if not data:
            print("Not found!")
            return
        music_items = data.get("results", [])
        if not music_items:
            print("Not found!")
            return
        found = False
        for idx, music in enumerate(music_items, start=1):
            song_name, artist_name, album_name, music_link = self.read_data(music)
            if self.track_name.lower() in song_name.lower():
                music_obj = Music(song_name, artist_name, album_name, music_link)
                print(f"Result {idx}:\n{music_obj}")
                found = True

        if not found:
            print("Not found!")

            

if __name__ == "__main__":
    track_name = input("Enter the track name to search: ").strip()
    if track_name:
        music_fetcher = MusicFetcher(track_name)
        music_fetcher.display_music_results()
