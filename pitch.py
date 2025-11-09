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

    def __init__(self, name, octave):
        self.name = name
        self.octave = octave

    @classmethod
    def from_string(cls, s):
        import re
        m = re.match(r'^([A-G](?:#|b)?)(\d+)$', s)
        if not m:
            raise ValueError(f'Invalid pitch string: {s}')
        note = m.group(1)
        octave = int(m.group(2))
        return cls(note, octave)

    def to_midi(self):
        base_num = self.NOTE_NAME_TO_NUM[self.name]
        return base_num + (self.octave + 1) * 12

    def __repr__(self):
        return f'{self.name}{self.octave}'

    def __eq__(self, other):
        return self.to_midi() == other.to_midi()

    def __lt__(self, other):
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
        name_new = self.NOTE_NAMES[note_num_new]
        return Pitch(name_new, octave_new)

if __name__ == '__main__':
    # 示例
    p1 = Pitch.from_string('E4')
    p2 = p1.transpose(1)   # 升半音
    p3 = p1.transpose(2)   # 升全音
    p4 = p1.transpose(-1)  # 降半音
    p5 = p1.transpose(12)  # 升八度

    print(p1)      # E4
    print(p2)      # F4
    print(p3)      # F#4
    print(p4)      # D#4
    print(p5)      # E5
