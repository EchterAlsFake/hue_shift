# Hue Shift

This repository contains a Python function that generates random colors and displays them in compatible terminals using ANSI escape codes.

## Installation

No external libraries are required. The function uses the built-in `colorsys` and `random` Python modules.

> pip install hue_shift

## Usage

To use the random color generator, simply call the `return_color()` function:

```python
print(f"{return_colour()}This is a random colour")
```
# Note

Not all terminals support this wide color range!
