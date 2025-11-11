import matplotlib.pyplot as plt


def plot_chord(fingering, chord_name='', base_fret=1, finger_numbers=None, barre=None):
    """
    绘制封闭矩形的吉他和弦图
    """
    strings = 6
    frets = 4
    string_space = 1.0
    fret_space = 1.0

    fig, ax = plt.subplots(figsize=(2.3, 4))

    # 指板框
    left = 0.5
    right = left + string_space * (strings - 1)
    top = frets * fret_space + 0.5
    bottom = 0.5

    # 画矩形框
    ax.plot([left, right], [top, top], color='black', lw=2)    # 顶线
    ax.plot([left, right], [bottom, bottom], color='black', lw=2)  # 底线
    ax.plot([left, left], [bottom, top], color='black', lw=2)
    ax.plot([right, right], [bottom, top], color='black', lw=2)

    # 画弦（竖线）
    for i in range(strings):
        x = left + i * string_space
        ax.plot([x, x], [bottom, top], color='black', lw=1)

    # 画品格（横线，不重复画最顶最底）
    for f in range(1, frets):
        y = top - f * fret_space
        ax.plot([left, right], [y, y], color='black', lw=1)

    # 弦标记X/O
    for i, val in enumerate(fingering):
        x = left + i * string_space
        if str(val).upper() == 'X':
            ax.text(x, top + 0.35, 'X', fontsize=12,
                    ha='center', va='center', color='red')
        elif val == 0:
            ax.text(x, top + 0.35, 'O', fontsize=12,
                    ha='center', va='center', color='green')

    # 按弦圆点 (1品到4品)
    for i, val in enumerate(fingering):
        if isinstance(val, int) and (val > 0):
            fret = val - base_fret + 1
            if 1 <= fret <= frets:
                x = left + i * string_space
                y = top - (fret - 0.5) * fret_space
                circ = plt.Circle(
                    (x, y), 0.22, color='#8242c4', ec='black', zorder=10)
                ax.add_patch(circ)
                if finger_numbers and finger_numbers[i]:
                    ax.text(x, y, str(
                        finger_numbers[i]), fontsize=8, ha='center', va='center', color='white', zorder=11)

    # 横按线
    if barre:
        fret = barre['fret'] - base_fret + 1
        if 1 <= fret <= frets:
            y = top - (fret - 0.5) * fret_space
            x1 = left + (barre['from_string'] - 1) * string_space
            x2 = left + (barre['to_string'] - 1) * string_space
            ax.plot([x1, x2], [y, y], lw=8, color='#a0522d',
                    solid_capstyle='round', zorder=9)

    # 和弦名字
    ax.text((left + right) / 2, top + 0.8, chord_name,
            fontsize=16, ha='center', va='center', weight='bold')
    # 品格标记
    if base_fret > 1:
        ax.text(right + 0.3, bottom, f'{base_fret}fr',
                fontsize=9, ha='left', va='bottom')

    ax.set_xlim(left - 0.5, right + 0.6)
    ax.set_ylim(bottom - 0.1, top + 1)
    ax.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # 示例：C和弦
    plot_chord(['X', 3, 2, 0, 1, 0], chord_name='C',
               finger_numbers=[None, 3, 2, None, 1, None])

# 示例：F大横按和弦
    plot_chord(['1', 3, 3, 2, 1, 1], chord_name='F',
               finger_numbers=[1, 3, 4, 2, 1, 1], barre={'fret': 1, 'from_string': 1, 'to_string': 6}, base_fret=1)
