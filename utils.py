from mido import MidiFile

def midi_sequence(path='midi.mid', sr=48000, hop_length=2048):
    #data = file.read()
    midi = MidiFile(path)

    melody = []

    for message in midi.play():
        if message.type == 'note_off':
            time = message.time
            note = message.note
            
            for i in range(int(time * sr / hop_length)):
                melody.append(note)

    return melody
