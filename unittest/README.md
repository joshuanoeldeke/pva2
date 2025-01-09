This is the command for running the docker container so it actually writes the metric logs and copies them out of the container before shutting down:

docker build -t python-test-metrics-unittest .   

docker run -v C:\Users\jnoeldeke\sourcecode\pva2\unittest\logs:/app/logs --cpus="1" -m 512m python-test-metrics-unittest