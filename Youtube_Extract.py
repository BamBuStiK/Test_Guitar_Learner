import youtube_dlc

Save_Path = "Saved_Vids"
custom_filename = "Test_Sample"

link = "https://www.youtube.com/watch?v=t6TsvbJ3Pos"

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': f'{Save_Path}/{custom_filename}.%(ext)s',  # Custom filename
    'nooverwrites': False,  # Allow overwriting existing files
}

with youtube_dlc.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([link])
        print('Video Downloaded Successfully!')
    except Exception as e:
        print("Error:", e)
        print("Some Errors!")
