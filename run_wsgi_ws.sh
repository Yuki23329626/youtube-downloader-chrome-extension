python3 -m gunicorn -D\
	--workers=1 \
	--threads=1 \
	wsgi:app \
	-b 0.0.0.0:5000
