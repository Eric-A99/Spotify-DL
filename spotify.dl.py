import os
import subprocess

def download_song():
    song_url = input("Enter the Spotify song URL: ")
    output_path = os.path.join(os.path.expanduser("~"), "Desktop", "Spotify Downloads")

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Change the current working directory to the output directory
    os.chdir(output_path)

    subprocess.run(["spotdl", song_url])

if __name__ == "__main__":
    download_song()
    print("Anotha One?")
    
