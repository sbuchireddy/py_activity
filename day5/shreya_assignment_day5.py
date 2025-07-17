songs_track = ["TrackA","TrackB","TrackC","TrackD"]

songs_track.remove("TrackC")
songs_track.insert(0,"TrackX")
songs_track.insert(1,songs_track.pop())
print(' '.join(songs_track))