build-hangman:
	docker build . -t hangman-py

xhost:
	xhost +	

run-windows:
	docker run --privileged -it --rm --cap-add=SYS_PTRACE -u 1000:1000 -e DISPLAY=127.0.0.1:0.0 -v D:\Download:/home/docker hangman-py