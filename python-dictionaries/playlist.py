playlist = {
    "title": "Summer Playlist",
    "author": "Nick Fuentes",
    "songs": [
        {
            "title": "Cute Without the 'E'",
            "artist": [
                "Taking Back Sunday"
            ],
            "duration": 2.45,
        },
        {
            "title": "Humble",
            "artist": [
                "Kendrick Lamar",
                "Skrillex"
            ],
            "duration": 3.40,
        },
        {
            "title": "30 for 30 Freestyle",
            "artist": [
                "Drake"
            ],
            "duration": 2.20,
        }
    ]
}

total_length = 0

for song in playlist["songs"]:
    total_length = total_length + song["duration"]
print(total_length)
