# ex08/Loading.py
import os


def ft_tqdm(lst: range):
    """Générateur avec animation circulaire optimisée."""
    total = len(lst)
    try:
        is_tty = os.isatty(1)
    except Exception:
        is_tty = False
    if not is_tty:
        for item in lst:
            yield item
        return
    CSI = "\033["
    RESET = f"{CSI}0m"
    HIDE = f"{CSI}?25l"
    SHOW = f"{CSI}?25h"
    GREEN = f"{CSI}38;5;46m"
    GRAY = f"{CSI}38;5;240m"
    CLEAR = f"{CSI}2K"
    POINTS = [
        (3, 0),
        (4, 1),
        (5, 2),
        (6, 3),
        (5, 4),
        (4, 5),
        (3, 6),
        (2, 5),
        (1, 4),
        (0, 3),
        (1, 2),
        (2, 1),
    ]
    H, W = 8, 7

    def move(r, c=1):
        return f"{CSI}{r};{c}H"

    def frame(p, f, cc, cur, tot):
        g = [[" "] * W for _ in range(7)]
        for i, (x, y) in enumerate(POINTS):
            g[y][x] = f"{GREEN if i < f else GRAY}●{RESET}"
        s = f"{p:3d}"
        g[3][2:5] = list(s)
        sc = max(1, cc - W // 2)
        lines = []
        for i, r in enumerate(g):
            lines.append(f"{move(base + i, 1)}{CLEAR}{move(base + i, sc)}{''.join(r)}")
        cnt = f"{cur}/{tot}"
        lines.append(
            f"{move(base + 7, 1)}{CLEAR}{move(base + 7, max(1, cc - len(cnt) // 2))}{cnt}"
        )
        return "".join(lines)

    try:
        ts = os.get_terminal_size()
        rows, cols = ts.lines, ts.columns
        base = rows - H - 1
        cc = cols // 2
    except OSError:
        base, cc = 1, 40
    print(f"{HIDE}\n" * H, end="", flush=True)
    try:
        for i, item in enumerate(lst, 1):
            p = (i * 100) // total
            f = (i * 12) // total
            print(frame(p, f, cc, i, total), end="", flush=True)
            yield item
    finally:
        print(f"{move(rows)}{SHOW}", end="", flush=True)
