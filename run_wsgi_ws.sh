python3 -m gunicorn -D\
	--workers=4 \
	--threads=4 \
	wsgi:app \
	-b 0.0.0.0:5000
