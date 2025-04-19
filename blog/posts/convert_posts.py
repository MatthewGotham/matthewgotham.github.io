# -*- coding: utf-8 -*-
"""
A script to convert all the markdown files in this folder to html.
@author: Matthew Gotham
"""

import os
import markdown

to_convert = [f for f in os.listdir('.') if f.endswith('md')
              and f"{f.split()[:-3]}.html" not in os.listdir('.')]
# Read markdown.
for md_filename in to_convert:
    with open(md_filename, 'r') as md_file:
        md = md_file.read()
        # \This/ is the conversion step.
        html = markdown.markdown(md)
        # Write html.
        html_filename = f"{md_filename[:-3]}.html"
        with open(html_filename, 'w') as html_file:
            html_file.write(html)
