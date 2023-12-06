flask_server_id=`ps -aux | grep flask_server.py | grep -v "grep" | grep -v "kill" | head -n 1 | awk '{print $2}'`

ps -aux | grep flask_server.py

echo flask_server_id = "$flask_server_id"

if [ "$flask_server_id" ]; then
	kill $flask_server_id
	echo "kill $flask_server_id"
fi

exit 0
