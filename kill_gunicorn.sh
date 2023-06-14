gunicorn_id=`ps -aux | grep gunicorn | head -n 1 | cut -d ' ' -f 3`

kill $gunicorn_id

exit 0