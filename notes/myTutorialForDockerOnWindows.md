# Use "Docker for Windows"
***
## The Environment
- VAIO Pro 13, SVP132A1CN
- Windows 10 Pro 64 bit
  * Version 1607 (OS Build 14393.576); comfirmed by *winver*
- Docker for Windows 1.12.5 (9503)

## Setup "Docker for Windows"
1. Download and execute "[Docker for Windows(stable)](https://docs.docker.com/docker-for-windows/#/download-docker-for-windows)"
2. Reboot Windows 10 to enable Hyper-V (if Hyper-V is disabled)
  * You can find the dialog window on https://www.kaitoy.xyz/2016/07/31/docker-for-windows/
3. Confirm that Docker is running after reboot
  * For my setup, "Unable to start: The VM couldn't get an IP address after 60 tries" error happened
    + After rebooting Windows 10 again, Docker was running correctly.
    + If the error would not be resolved by the reboot, the [workaround](https://github.com/docker/for-win/issues/54#issuecomment-257157813) I found would be necessary
4. Open command prompt and check the version of docker commands below
  * *docker --version*
  * *docker-compose --version*
  * *docker-machine --version*
5. Run *docker run hello-world* on the command prompt. Outputting messages below means docker is running correctly

```
C:\Users\kaito>docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world

c04b14da8d14: Pull complete
Digest: sha256:0256e8a36e2070f7bf2d0b0763dbabdd67798512411de4cdcf9431a1feb60fd9
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker Hub account:
 https://hub.docker.com

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

## References
- https://docs.docker.com/docker-for-windows/
