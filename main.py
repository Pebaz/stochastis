# Turn notes into sheet music: http://web.mit.edu/music21/doc/about/what.html


import sys
from tempfile import NamedTemporaryFile
from pathlib import Path


NOTES = list(range(55, 100))
TOTAL_NOTES = len(NOTES)


def instructions(func):
    return [
        (i % TOTAL_NOTES if i != 0 else i)
        for i in func.__code__.co_code
    ]


def get_all_notes(module_filename):
    notes = []

    import importlib.util
    spec = importlib.util.spec_from_file_location(
        Path(module_filename).stem,
        module_filename
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for obj in module.__dict__.values():
        if hasattr(obj, '__code__'):
            notes.extend(instructions(obj))

    return notes


def populate_notes(mf, code):
    for i, note in enumerate(code):
        if note == 1:
            mf.addNote(
                track=0,
                channel=0,
                pitch=NOTES[note],
                time=i / 3.0,
                duration=1 / 3.0,
                volume=100
            )

            mf.addNote(
                track=0,
                channel=0,
                pitch=NOTES[note ** 2 % TOTAL_NOTES],
                time=i / 3.0,
                duration=1 / 3.0,
                volume=100
            )
            continue

        elif note == 0:
            continue

        mf.addNote(
            track=0,
            channel=0,
            pitch=NOTES[note],
            time=i / 3.0,
            duration=1 / 3.0,
            volume=100
        )


def play_midi_file(midi_filename):
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 1024
    import pygame
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(0.8)

    try:
        clock = pygame.time.Clock()
        pygame.mixer.music.load(midi_filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)
    except KeyboardInterrupt:
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.stop()
        raise SystemExit
    
    raise SystemExit


def output_music(module_filename, output_filename):
    code = get_all_notes(module_filename)

    from midiutil import MIDIFile
    mf = MIDIFile(1)     # only 1 track
    start_time = 0
    track = 0
    mf.addTrackName(track, start_time, "Sample Track")
    mf.addTempo(track, start_time, 120)

    populate_notes(mf, code)

    with open(output_filename, 'wb') as file:
        mf.writeFile(file)


def play_music(filename):
    path = Path(filename)

    if path.suffix == '.py':
        temp_file = NamedTemporaryFile(mode='wb', suffix='.mid', delete=False)
        temp_file.close()
        output_music(filename, temp_file.name)
        play_midi_file(temp_file.name)

    elif path.suffix == '.mid':
        play_midi_file(filename)

    else:
        raise Exception('File type not supported:', path.suffix)


def main(args=None):
    args = args or sys.argv[1:]

    # stochastis some_file.py --out foo.mid  # Generate only
    if len(args) == 3:
        filename, __out, output_filename = args
        assert Path(output_filename).suffix == '.mid', 'use .mid output type'
        output_music(filename, output_filename)

    # stochastis foo.mid  # Play from file
    # stochastis some_file.py  # Generate and play from file
    elif len(args) == 1:
        play_music(args[0])

    else:
        print(
            'Usage:\n'
            '  stochastis some_file.py --out foo.mid  # Generate only\n'
            '  stochastis foo.mid  # Play from file\n'
            '  stochastis some_file.py  # Generate and play from file\n'
        )


if __name__ == '__main__':
    main(sys.argv[1:])
