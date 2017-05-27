PID=$$

kill_childs() {
    killall python3
}

trap 'kill_childs' SIGINT SIGTERM

image_load="$1"
xoffset="$2"
yoffset="$3"

cores=64
for i in `seq 1 $cores`; do
    nohup python3 pixelflood.py "$image_load" 1000 0 16&
done

echo $!

ps -axf | grep $PID

for pid in `seq 1 $cores`; do
    echo $pid
    #wait $pid
done


