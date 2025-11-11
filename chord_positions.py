from chord import Chord
from fretboard import Fretboard


def find_chord_positions(fretboard: Fretboard, chord: Chord, max_fret: int = 22):
    """
    Identifies possible fretboard positions for playing a given chord.

    This function calculates the positions on a guitar fretboard where the notes 
    of a specified chord can be played, up to a given maximum fret. It marks the 
    root note of the chord with 'r' and other chord notes with 'x'. Unused positions 
    are marked with '-'.

    Args:
        fretboard (Fretboard): The Fretboard object representing the guitar's layout.
        chord (Chord): The Chord object containing the notes and root of the chord.
        max_fret (int, optional): The highest fret to consider. Defaults to 22.

    Returns:
        List[Optional[str]]: A list of strings representing the fretboard positions 
        for each string. The first element is `None` to align with string indexing 
        starting from 0. Each string contains 'r' for root notes, 'x' for other 
        chord notes, and '-' for unused positions.
    """
    matched = [['-' for _ in range(max_fret + 1)]
               for _ in fretboard.open_strings]
    chord_notes = set(e.note for e in chord.notes)
    root_note = chord.root.note
    for string_index in range(1, 6 + 1):
        open_pitch = fretboard.get_pitch(string_index, 0)
        for semitone in range(max_fret + 1):
            pitch_at_fret = open_pitch + semitone
            if pitch_at_fret.note in chord_notes:
                matched[string_index -
                        1][semitone] = 'r' if pitch_at_fret.note == root_note else 'x'
    matched = [''.join(e) for e in matched]
    return matched


def get_chord_finger_placements(matched):
    # find the minimal fret span that covers all chord notes
    num_strings = len(matched)
    root_positions = []
    for i in range(num_strings - 3, num_strings):
        t = matched[i].find('r')
        if t != -1:
            root_positions.append((i, t))
    root_positions.sort(key=lambda x: (x[1], -x[0]))
    return root_positions


if __name__ == "__main__":
    fretboard = Fretboard()
    for root, name in [('C3', 'major'), ('D3', 'minor'), ('E3', 'minor'), ('F3', 'major'), ('G3', 'major'), ('A3', 'minor')]:
        chord = Chord(root, name)
        print(chord.abbr)
        positions = find_chord_positions(fretboard, chord)
        print('\n'.join(positions))
        placement = get_chord_finger_placements(positions)
        print(placement)
        # break
