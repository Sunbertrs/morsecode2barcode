# morsecode2barcode

A little Python program to convert your morse code to a barcode-like graph.

To use this program, just easily change a few definitions in the file.

- `codes`: List, every items in the list are in string, and the morse code follows a format, like:
  - ` `: A space to split a character.
  - `/`: A slash to split a word.

- `border`: Interger, to set the border surround the barcode.

- `height`: Interger, to set the height of the barcode.

- `line_width`: Interger, to set the default width of the barcode.
  - A `.` will takes a default width, and `-` will takes double of default.
  - ` ` also takes double of default.

- `separate_per_line`: Every items between `codes` will separate by this value.
