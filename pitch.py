import re


class Pitch:
    NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    NOTE_NAME_TO_NUM = {
        'C': 0, 'C#':1, 'Db':1,
        'D': 2, 'D#':3, 'Eb':3,
        'E': 4, 'Fb':4,
        'F': 5, 'F#':6, 'Gb':6,
        'G': 7, 'G#':8, 'Ab':8,
        'A': 9, 'A#':10, 'Bb':10,
        'B': 11, 'Cb':11
    }
    NUM_TO_NAME = {v: k for k, v in NOTE_NAME_TO_NUM.items() if len(k) <= 2 and '#' in k or 'b' not in k}

    def __init__(self, name):
        m = re.match(r'^([A-G](?:#|b)?)(\d+)$', name)
        if not m:
            raise ValueError(f'Invalid pitch string: {s}')
        note = m.group(1)
        octave = int(m.group(2))
        self.note = note
        self.octave = octave

    def to_midi(self):
        base_num = self.NOTE_NAME_TO_NUM[self.note]
        return base_num + (self.octave + 1) * 12

    def __repr__(self):
        return f'{self.note}{self.octave}'

    def __eq__(self, other):
        if isinstance(other, str):
            other = Pitch(other)
        return self.to_midi() == other.to_midi()

    def __lt__(self, other):
        if isinstance(other, str):
            other = Pitch(other)
        return self.to_midi() < other.to_midi()

    def __hash__(self):
        return hash(self.to_midi())

    def transpose(self, semitones):
        """
        参数 semitones 正负都可以（+1：升半音，-1：降半音，+2/+12即全音/八度）
        返回新Pitch对象
        """
        midi = self.to_midi() + semitones
        octave_new = midi // 12 - 1
        note_num_new = midi % 12
        # 默认输出#而不是b，简化
        note_new = self.NOTE_NAMES[note_num_new]
        return Pitch(note_new + str(octave_new))

    def __add__(self, semitones):
        """
        升半音等同于加正数
        """
        return self.transpose(semitones)

    def __sub__(self, semitones):
        """
        降半音等同于加负数
        """
        return self.transpose(-semitones)


if __name__ == '__main__':
    # 示例
    p1 = Pitch('E4')
    p2 = p1 + 1   # 升半音
    p3 = p1 + 2   # 升全音
    p4 = p1 - 1  # 降半音
    p5 = p1 + 12  # 升八度

    assert p1 == 'E4'
    assert p2 == 'F4'
    assert p3 == 'F#4'
    assert p4 == 'D#4'
    assert p5 == 'E5'
