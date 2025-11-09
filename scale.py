from pitch import Pitch


class ScaleType:
    MAJOR = [2, 2, 1, 2, 2, 2, 1]


class Scale:
    def __init__(self, tonic, scale_type):
        if isinstance(tonic, str):
            tonic = Pitch(tonic)
        self.tonic = tonic

        self.scale_type = scale_type
        self.notes = []
        note = tonic
        for interval in scale_type:
            self.notes.append(note)
            note = note + interval

    def __repr__(self):
        return f'{self.notes}'

    def transpose(self, semitones):
        """
        Transpose the scale by a given number of semitones.
        Returns a new Scale object.
        """
        new_tonic = self.tonic + semitones
        return Scale(new_tonic, self.scale_type)

    def __add__(self, semitones):
        """
        Transpose the scale by a given number of semitones.
        Equivalent to calling transpose.
        """
        return self.transpose(semitones)

    def __sub__(self, semitones):
        """
        Transpose the scale down by a given number of semitones.
        Equivalent to calling transpose with negative semitones.
        """
        return self.transpose(-semitones)


if __name__ == '__main__':
    scale = Scale('C3', ScaleType.MAJOR)
    for semitones in ScaleType.MAJOR:
        print(scale.tonic, scale)
        scale += semitones
