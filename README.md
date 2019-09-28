# Python Flask in Docker#

Build the image using the following command

```bash
docker build -t flask:latest .
```

Run the Docker container using the command shown below.

```bash
docker run -d -p 5000:5000 flask:latest 
```

Log into the Docker Hub from the command line
```bash
docker login
```

Check the image ID
```bash
docker images
```
what you will see will be similar to this
```bash
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
flask               latest              bfddf916c984        1 minutes ago      110MB
```

Tag your image
```bash
docker tag <IMAGE ID> yourdockerhubusername/flask:latest
```
Push your image to the repository
```bash
docker push yourdockerhubusername/flask:latest
```
Run Docker App
```bash
docker run yourdockerhubusername/flask:latest
```
