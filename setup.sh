#!/bin/bash
sudo apt-get update
sudo apt-get install git python3-pip python3-pillow python3-pip

hook_file='.git/hooks/post-commit'
echo '#!/bin/bash' > "$hook_file"
echo 'echo Running $BASH_SOURCE' > "$hook_file"
echo 'set | egrep GIT' > "$hook_file"
echo 'echo PWD is $PWD' > "$hook_file"

