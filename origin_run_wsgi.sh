if [ "$DOMAIN_NAME" = "" ]
then
  echo "\nYou should set your DOMAIN_NAME at first"
  echo "\ne.g.: export DOMAIN_NAME=\"the_domain_name_you_want\"\n"
  exit 0
fi

gunicorn -D\
	--workers=4 \
	--threads=4 \
	wsgi:app \
	-b 0.0.0.0:5000 \
	--certfile="/etc/letsencrypt/archive/$DOMAIN_NAME-0003/fullchain1.pem" \
	--keyfile="/etc/letsencrypt/archive/$DOMAIN_NAME-0003/privkey1.pem"
