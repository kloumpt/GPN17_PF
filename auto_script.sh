#!/bin/bash

if [ $USER == 'serge' ]; then
    exit
fi

git checkout -- .
git pull

source params.sh

python3 pixelflood_gen.py "$image" "$xoffset" "$yoffset" 1
killall python3
python3 pixelflood.py "$threads"

