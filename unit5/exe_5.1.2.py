import winsound


def play_song():
    freqs = {
        "la": 220,
        "si": 247,
        "do": 261,
        "re": 293,
        "mi": 329,
        "fa": 349,
        "sol": 392,
    }

    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

    note_list = notes.split("-")
    print(dir(note_list))
    for note in note_list:
        name, duration = note.split(",")
        frequency = freqs[name]
        duration = int(duration)
        winsound.Beep(frequency, duration)


if __name__ == '__main__':
    play_song()

