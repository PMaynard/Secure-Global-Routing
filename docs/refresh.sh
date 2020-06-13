
while inotifywait -e close_write *.md figures/*.gv; do make; done