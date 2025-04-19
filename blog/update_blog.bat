@echo off
cd posts
python convert_posts.py
cd ..
python build_page.py