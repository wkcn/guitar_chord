from interval import Interval


class Chord:
    def __init__(self, root, intervals):
        self.root = root
        self.intervals = intervals
        self.notes = self._build_chord()

    def _build_chord(self):
        notes = [self.root]
        for interval in self.intervals:
            note = self.root + interval
            notes.append(note)
        return notes

    def __repr__(self):
        return f'Chord(notes={self.notes})'


class MajorChord(Chord):
    def __init__(self, root):
        super().__init__(root, [Interval.M3, Interval.P5])  # Major chord: root, major third, perfect fifth


if __name__ == "__main__":
    from pitch import Pitch
    root = Pitch('C3')
    c_major = MajorChord(root)
    print(c_major)  # Should print the notes of the C major chord
