PID=$$

kill_childs() {
    killall python3
    kill -9 $PID
    exit
}

trap 'kill_childs' SIGINT SIGTERM


cores=16
for i in `seq 1 $cores`; do
    python3 pixelflood.py  16&
done

while [[ 1 -eq 1 ]]
do
    sleep 1
done



