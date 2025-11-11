from typing import List
from pitch import Pitch


class Fretboard:
    STANDARD_TUNING = ["E2", "A2", "D3", "G3", "B3", "E4"]

    def __init__(self, open_strings: List[str] = None):
        self.open_strings = [Pitch(n) for n in (
            open_strings or self.STANDARD_TUNING)]

    def get_pitch(self, string: int, fret: int) -> Pitch:
        """
        string: 6为最粗弦(低音E2)，1为最细弦(高音E4)
        fret: 品格（0为空弦）
        返回值是Pitch对象
        """
        base = self.open_strings[6 - string]  # 以弦号从6到1排列（最粗到最细）
        return base + fret


if __name__ == '__main__':
    # ==== 测试用法 ====
    fb = Fretboard()
    assert fb.get_pitch(6, 0) == Pitch('E2')
    assert fb.get_pitch(6, 1) == Pitch('F2')
    assert fb.get_pitch(1, 0) == Pitch('E4')
    assert fb.get_pitch(3, 2) == Pitch('A3')
    assert fb.get_pitch(2, 3) == Pitch('D4')

    # 自定义调弦（例如降半音调音）
    custom = ["Eb2", "Ab2", "Db3", "Gb3", "Bb3", "Eb4"]
    fb2 = Fretboard(custom)
    assert fb2.get_pitch(6, 5) == Pitch('Ab2')  # Ab2（第6弦+5品）
