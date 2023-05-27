
class MusicNotes:
    def __init__(self):
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 34:
            raise StopIteration()
        self.index += 1
        self.notes.append(self.notes[self.index]*2)
        return self.notes[self.index]


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)

        
if __name__ == '__main__':
    main()
