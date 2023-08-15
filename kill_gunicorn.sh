gunicorn_id=`ps -aux | grep gunicorn | grep -v "grep" | head -n 1 | awk '{print $2}'`

kill $gunicorn_id

exit 0
