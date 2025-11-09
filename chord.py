from interval import Interval as I


class Chord:
    def __init__(self, root, intervals):
        self.root = root
        self.intervals = intervals
        self.notes = self._build_chord()

    def _build_chord(self):
        notes = []
        for interval in self.intervals:
            note = self.root + interval
            notes.append(note)
        return notes

    def __repr__(self):
        return f'Chord(notes={self.notes})'


CHORD_RECIPES = {
    'major': [I.P1, I.M3, I.P5],
    'minor': [I.P1, I.m3, I.P5],
}


def get_chord(root, name):
    if name not in CHORD_RECIPES:
        raise ValueError(f"Chord '{name}' is not defined.")
    intervals = CHORD_RECIPES[name]
    return Chord(root, intervals)


if __name__ == "__main__":
    from pitch import Pitch
    root = Pitch('C3')
    c_major = get_chord(root, 'major')
    print(c_major)  # Should print the notes of the C major chord
