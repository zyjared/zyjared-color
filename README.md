# zyjared-color

Personal font color utility library for Python, primarily used in PowerShell.

## Installation

```sh
pip install zyjared-color
```

## Usage

### Basic Usage

Create a styled text using the `Color` class:

```python
text = Color('Hello World!').red().bold()
print(text)
```

You can achieve the same result using `ColorStatic` class methods:

```python
from zyjared_color import ColorStatic as Colors

text = Colors.red('Hello World!').bold()
print(text)
```

Or using convenience functions for styles:

```python
from zyjared_color import red, bold, italic

text = red('Hello World!').bold()
print(text)

text = italic(text)
print(text)
```

### Chaining Usage

You can chain multiple style methods together:

```python
from zyjared_color import red

text = red('Hello World!').bold().italic().underline().through()
print(text)
```

### Nested Usage

Combine different styling methods and functions:

```python
from zyjared_color import red, bold, italic, underline, through, blue

text = through(underline(italic(bold(red('Hello World!')))))
print(text)

# add more text
text = text + ' !!! ' + blue('Hello World!')
print(text)

# change text color
text.yellow()
print(text)
```

## All Styles

You can view all styles through the `ColorStatic` class method.

### styles

- `bold`
- `dim`
- `italic`
- `underline`
- `through`
- `reverse`
- `blink`
- `blink_fast`
- `hidden`

### frontground

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `bright_black`
- `bright_red`
- `bright_green`
- `bright_yellow`
- `bright_blue`
- `bright_magenta`
- `bright_cyan`
- `bright_white`

### background

- `bg_black`
- `bg_red`
- `bg_green`
- `bg_yellow`
- `bg_blue`
- `bg_magenta`
- `bg_cyan`
- `bg_white`
- `bg_bright_black`
- `bg_bright_red`
- `bg_bright_green`
- `bg_bright_yellow`
- `bg_bright_blue`
- `bg_bright_magenta`
- `bg_bright_cyan`
- `bg_bright_white`
