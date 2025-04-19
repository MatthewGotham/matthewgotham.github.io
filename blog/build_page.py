# -*- coding: utf-8 -*-
"""
A script to build my blog from individual html files as posts.
@author: Matthew Gotham
"""

import os

# Make the top of the page.
page_html = """<html lang="en-GB">
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="../gothstyle.css">
        <base target="_blank">
        <title>Matthew Gotham: Blog</title>
    </head>

    <body>
        <nav>
            <p><a href=".." target="_self">Home</a></p>
            <p>Blog</p>
            <p><a href="../linguistics" target="_self">Linguistics</a></p>
        </nav>

        <main>
            <h1>Matthew Gotham</h1>
            <h2>Blog</h2>
            <hr>
"""

# Add the blog posts.
posts = [os.path.join('posts', f) for f in os.listdir('./posts')
         if f.endswith('_raw.html')]
# Post filenames have to start YYYY-MM-DD for \this/ to work.
for post in sorted(posts, reverse=True):
    with open(post, 'r') as post_html:
        page_html += post_html.read()
        page_html += '<hr>'

# Make the bottom of the page.
page_html += """
        </main>
    </body>
</html>"""

# Write the page.
with open('index.html', 'w') as page:
    page.write(page_html)
