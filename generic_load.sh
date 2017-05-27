PID=$$

kill_childs() {
    killall python3
    kill -9 $PID
    exit
}

trap 'kill_childs' SIGINT SIGTERM

image_load="$1"
xoffset="$2"
yoffset="$3"

cores=128
for i in `seq 1 $cores`; do
    nohup python3 pixelflood.py "$image_load" $xoffset $yoffset 16&
done

while 1;do;done



