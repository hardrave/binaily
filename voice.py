import vlc
import time

def talk(recording):
    # Create a VLC media player instance
    p = vlc.MediaPlayer(recording)

    # Start playing the media
    p.play()

    # Allow some time for the media to start playing
    time.sleep(0.5)

    # Get the media duration
    duration = p.get_length() / 1000  # Duration in seconds

    # If the duration is not available, set a default value
    if duration <= 0:
        duration = 10  # Set to a reasonable default duration

    # Sleep for the duration of the media
    time.sleep(duration)