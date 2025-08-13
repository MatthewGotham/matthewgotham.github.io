# -*- coding: utf-8 -*-
"""
A script to convert all the markdown files in this folder to html. We
need two versions: one for the general blog page, and one for the
standalone post page.
@author: Matthew Gotham
"""

import os
import markdown

blog_opening = """<html lang="en-GB">
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../../gothstyle.css">
        <base target="_blank">
        <title>Matthew Gotham: Blog</title>
    </head>

    <body>
        <nav>
            <p><a href="../.." target="_self">Home</a></p>
            <p><a href=".." target="_self">Blog</a></p>
            <p><a href="../../linguistics" target="_self">Linguistics</a></p>
        </nav>

        <main>
            <h1>Matthew Gotham</h1>
            <h2>Blog</h2>
            <hr>
"""

blog_closing = """
        </main>
    </body>
</html>
"""

to_convert = [f for f in os.listdir('.') if f.endswith('md')
              and f"{f[:-3]}.html" not in os.listdir('.')]
# Read markdown.
for md_filename in to_convert:
    print(f"Converting {md_filename}", end='... ')
    with open(md_filename, 'r') as md_file:
        md = md_file.read()
        # \This/ is the conversion step.
        html_minimal = markdown.markdown(md).replace("`", "&lsquo;"
                                                     ).replace("'", "&rsquo;")
        html_filename = f"{md_filename[:-3]}.html"
        link = f'./posts/{html_filename}'
        # Hyperlink in the title:
        html_raw = html_minimal.replace('>', f'><a href="{link}">',
                                        1).replace('</', '</a></', 1)
        # Individual post:
        html = blog_opening+html_minimal+blog_closing
        # Write html.
        html_filename = f"{md_filename[:-3]}.html" # individual post
        with open(html_filename, 'w') as html_file:
            html_file.write(html)
        raw_filename = f"{md_filename[:-3]}_raw.html"
        with open(raw_filename, 'w') as raw_file:
            raw_file.write(html_raw)
    print("complete.")
