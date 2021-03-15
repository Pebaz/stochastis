import mido
out = mido.open_output('UM_ONE')
loop = mido.MidiFile('output.mid')
for msg in loop.play():
    msg.channel = 9  # Channel is 1 by default, set to MIDI percussion channel 10
    out.send(msg)







# import pygame

# def play_music(midi_filename):
#     '''Stream music_file in a blocking manner'''
#     clock = pygame.time.Clock()
#     pygame.mixer.music.load(midi_filename)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         clock.tick(30) # check if playback has finished

# midi_filename = 'output.mid'

# # mixer config
# freq = 44100  # audio CD quality
# bitsize = -16   # unsigned 16 bit
# channels = 2  # 1 is mono, 2 is stereo
# buffer = 1024   # number of samples
# pygame.mixer.init(freq, bitsize, channels, buffer)

# # optional volume 0 to 1.0
# pygame.mixer.music.set_volume(0.8)

# # listen for interruptions
# try:
#     # use the midi file you just saved
#     play_music(midi_filename)
# except KeyboardInterrupt:
#     # if user hits Ctrl/C then exit
#     # (works only in console mode)
#     pygame.mixer.music.fadeout(1000)
#     pygame.mixer.music.stop()
#     raise SystemExit
