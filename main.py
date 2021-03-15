
# Turn notes into sheet music: http://web.mit.edu/music21/doc/about/what.html


from midiutil import MIDIFile

# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 2             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 4             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)




def instructions(func):
    from dis import Bytecode

    dis = Bytecode(func)
    print(dis.dis())

    instructions_with_line_numbers = [
        line.split()
        for line in dis.dis().splitlines()
    ]

    # Use line numbers as time info to play many notes at once
    print(instructions_with_line_numbers)

    instructions = []
    for line in dis.dis().splitlines():
        possible_inst = [i for i in line.split() if i.isidentifier()]
        instructions.extend(possible_inst)
    
    return instructions

def music(a, b, c):
    a + b
    b + c
    c + a
    a * b * c
    a + b * c ** a

print(instructions(music))
