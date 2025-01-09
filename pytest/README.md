This is the command for running the docker container so it actually writes the metric logs and copies them out of the container before shutting down:

docker run -v C:\Users\jnoeldeke\sourcecode\pva2\pytest\logs:/app/logs python-test-metrics