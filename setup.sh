#!/bin/bash
sudo apt-get update
sudo apt-get install git python3-pip python3-pillow python3-pip

hook_file='.git/hooks/post-commit'
echo '#!/bin/bash' > "$hook_file"
echo 'touch /root/GPN17_PF/post_commit_successful' >> "$hook_file"

