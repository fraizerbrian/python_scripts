#install pandoc

FILES=*.html
for f in $FILES
do
    filename="${f%.*}"
    echo "Converting $f to $filename.md"
done