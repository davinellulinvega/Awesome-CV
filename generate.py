#!/usr/bin/python3
import json

# Import font awesome metadata file
with open("Font-Awesome/advanced-options/metadata/icons.json", "r") as meta_file:
    metadata = json.load(meta_file)

# Write the sty file
with open("fontawesome.sty", "w") as sty_file:
    sty_file.write("% Identify this package.\n")
    sty_file.write("\\NeedsTeXFormat{LaTeX2e}\n")
    sty_file.write("\\ProvidesPackage{fontawesome}[Font awesome icons]\n")
    sty_file.write("% Requirements to use.\n")
    sty_file.write("\\usepackage{fontspec}\n\n")
    sty_file.write("% Generic command displaying an icon by its name.\n")
    sty_file.write("\\newcommand*{\\faicon}[1]{{\n")
    sty_file.write("\\FA\csname faicon@#1\endcsname\n")
    sty_file.write("}}\n")

    for name, attrs in metadata.items():
        sty_file.write('\\expandafter\\def\\csname faicon@')
        sty_file.write(name)
        sty_file.write('\\endcsname {\\symbol{"')
        sty_file.write(attrs['unicode'].upper())
        sty_file.write('}} \\def\\fa')
        sty_file.write(''.join([el.capitalize() for el in name.split('-')]))
        sty_file.write(' {{\\FA\\csname faicon@')
        sty_file.write(name)
        sty_file.write('\\endcsname}}\n')
