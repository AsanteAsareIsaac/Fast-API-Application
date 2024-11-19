# pull the python base image
FROM python:3.11-alpine

# set the working directory. Location in the container which holds your application
WORKDIR /app

# copy the dependencies list file to avoid recreating the image when the code changes but dependencies doesn't
COPY requirements.txt .

# install the app packages
RUN pip install -r requirements.txt

# copy the source code into working directory in the container
COPY . .

# run the application
CMD uvicorn app:app --host 0.0.0.0 --port 80 --reload