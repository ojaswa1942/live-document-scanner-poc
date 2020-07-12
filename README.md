# live-document-scanner-poc

Proof of concept for Live Document Scanner (Video Stream)

Steps for photograph:
- Edge detection
- Find contours 
- Apply perspective transform
- Apply filters for better view


To run live:
- Git clone
- Move into repository folder
- Run `docker build --tag scanner-poc:1.1 .`

If you're using X-Server:
- Run `xhost +`
- Run `sudo docker run --rm -ti --net=host --ipc=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --device=/dev/video0:/dev/video0 --env="QT_X11_NO_MITSHM=1" scanner-poc:1.1`