## Pre-requisites:
* [hey](https://github.com/rakyll/hey)

## Steps to reproduce:


1. Build the docker image:
    ```sh
    docker build . -t fastapi-bug:latest
    ```

2. Run it:
    ```sh
    docker run --rm -it -p 80:80 fastapi-bug:latest
    ```
   
3. Run load test
    ```sh
    hey -D input.json -m POST -n 1000 -c 50 http://localhost:80/
    ```