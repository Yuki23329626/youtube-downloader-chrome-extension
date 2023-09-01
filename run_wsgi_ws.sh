#!/bin/bash

# List of package names to check
package_names="flask yt_dlp gunicorn"

for package_name in $package_names; do
    if pip3 show "$package_name" > /dev/null 2>&1; then
        echo "$package_name is installed."
    else
        echo "\n$package_name is not installed."
	echo "Installing $package_name...\n"
	if [ "$package_name" = "flask" ]; then
		pip3 install flask[async]
	fi
        pip install "$package_name"
    fi
done

python3 -m gunicorn -D\
	--workers=1 \
	--threads=1 \
	wsgi:app \
	-b 0.0.0.0:5000
