"""PyAudio Example: Play a wave file (callback version)."""

#import pyaudio
import wave
import time
import os.path
from problems.Errors import CLI_Audio_File_Exception

class Player:
    """Class to play files"""

    def __init__(self):
        """Initialize the class"""
        self.currentSong = "Nothing playing."
        self.paused = True
        self.position = 0

    def getCurrentSong(self):
        """Getter to return current song"""
        return self.currentSong

    def pause(self):
        """Starts or stops playing the song"""
        if self.paused == False:
            self.paused = True
#            self.stream.stop_stream()
        else:
            self.paused = False
#            self.stream.start_stream()

    def play(self, track):
        """Play a file"""
        try:
            #verify valid file name
            if os.path.isfile (track):
                self.paused = False
                self.currentSong = track
                self.wf = wave.open(track, 'rb')
            else:
                #flag invalid file
                raise CLI_Audio_File_Exception
        except CLI_Audio_File_Exception:
            #ignore invalid file names
            pass
        except wave.Error:
            print("problem with .wav file")
            pass
         
# I commened this out so i could run it on my laptop
#        try:
#            # instantiate PyAudio (1)
#            self.p = pyaudio.PyAudio()
#
#            # open self.stream using callback (3)
#            self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
#                    channels=self.wf.getnchannels(),
#                    rate=self.wf.getframerate(),
#                    output=True,
#                    stream_callback=self.callback)
#
#            # start the self.stream (4)
#            self.stream.start_stream()
#        except CLI_Audio_File_Exception:
#            print("File failed to load")
#            pass
#        except: 
#            print("other")
#            pass

    def stop(self):
        """Stop song playing"""
#        self.stream.stop_stream()
#        self.stream.close()
        self.wf.close()

#        self.p.terminate() 

#    def callback(self, in_data, frame_count, time_info, status):
        """Callback for open stream"""
#        data = self.wf.readframes(frame_count)
#        return (data, pyaudio.paContinue)

