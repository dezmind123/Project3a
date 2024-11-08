#USe offical oython imae as the base image 
FROM python:3.8-slim-buster

#set working diectory in container to /app
WORKDIR /app

#copy contents of the current dirctory into the container
COPY . /app

#upgrade pip
RUN pip install --upgrade pip

#install any needed packages 
RUN pip install --no-cache-dir -r requirments.txt

#set default comnds to reun when starting the container
CMD ["python", "app.py"]