PID=$$

kill_childs() {
    killall python3
}

trap 'kill_childs' SIGINT SIGTERM


cores=64
for i in `seq 1 $cores`; do
    nohup python3 pixelflood.py black.png 1000 0 16&
done

echo $!

ps -axf | grep $PID

for pid in `seq 1 $cores`; do
    echo $pid
    #wait $pid
done


