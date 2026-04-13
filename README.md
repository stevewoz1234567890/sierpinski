# Sierpinski Triangle (Pygame)

Recursive drawing of a [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle) using Python and Pygame. The program subdivides a triangle by edge midpoints, then repeats the same rule on each of the three corner triangles until the requested **degree** is reached.

## Requirements

- Python 3
- [Pygame](https://www.pygame.org/)

## Install Pygame

Use a normal terminal or command prompt (not IDLE’s interactive shell).

**Windows**

```text
py -3 -m pip install pygame --user
```

**macOS**

```text
python3 -m pip install pygame --user
```

**Linux** (many distributions block system-wide `pip`; a virtual environment is reliable)

```text
python3 -m venv .venv
source .venv/bin/activate
pip install pygame
```

## Run

From this directory:

```text
python3 sierpinski.py
```

Close the window to quit.

## Customize

In `sierpinski.py`, inside `main()`:

- **`degree`** — how many further subdivision levels to apply after drawing each triangle (higher values draw more detail; large values can be slow because of many `pygame.display.flip()` calls).
- **`initial_color`** — e.g. `BLACK`, `RED`, `GREEN`, `BLUE`.
- **`initial_line_width`** — positive integer for outline width; **`0`** fills triangles with the chosen color instead of outlining them.

## Implementation notes

- **`find_midpoint(p1, p2)`** returns the midpoint of two `[x, y]` points.
- **`sierpinski(degree, p1, p2, p3, color, line_width, screen)`** draws the current triangle, stops if `degree == 0`, otherwise computes midpoints and recurses into the three corner triangles with `degree - 1`.

The similarity dimension of the ideal Sierpinski gasket is log(3)/log(2) ≈ 1.585: three self-similar pieces, each scaled by 1/2 in each direction.
