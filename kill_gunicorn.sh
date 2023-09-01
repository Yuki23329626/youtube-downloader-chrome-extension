gunicorn_id=`ps -aux | grep gunicorn | grep -v "grep" | grep -v "kill" | head -n 1 | awk '{print $2}'`

ps -aux | grep gunicorn

echo gunicorn_id = "$gunicorn_id"

if [ "$gunicorn_id" ]; then
	kill $gunicorn_id
	echo "kill $gunicorn_id"
fi

exit 0
