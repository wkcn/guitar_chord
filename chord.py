from interval import Interval as I
from pitch import Pitch


CHORD_RECIPES = {
    'major': [I.P1, I.M3, I.P5],
    'minor': [I.P1, I.m3, I.P5],
}


CHORD_ABBRS = {
    'major': '',
    'minor': 'm',
}


class Chord:
    def __init__(self, root, name):
        if isinstance(root, str):
            root = Pitch(root)
        self.root = root
        self.name = name
        self.notes = self._build_chord()
        self.abbr = root.note + CHORD_ABBRS[name]

    def _build_chord(self):
        notes = []
        intervals = CHORD_RECIPES[self.name]
        for interval in intervals:
            note = self.root + interval
            notes.append(note)
        return notes

    def __repr__(self):
        return f'Chord(name="{self.name}", notes={self.notes}, abbr="{self.abbr}")'


if __name__ == "__main__":
    c_major = Chord('C3', 'major')
    print(c_major)  # Should print the notes of the C major chord
    d_minor = Chord('D3', 'minor')
    print(d_minor)  # Should print the notes of the D minor chord
