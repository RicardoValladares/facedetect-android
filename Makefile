
push:
	git status
	git add .
	git commit -m "$$(date)"
	git pull origin main 
	git push origin main

run:
	python main.py

dependens:
	apt-get install -y python3-pip build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
	apt-get install -y libgstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good
	apt-get install -y build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6
	apt-get install -y libffi-dev
	pip install buildozer
	pip install cython==0.29.35
	pip install Kivy

android:
	buildozer -v android debug

