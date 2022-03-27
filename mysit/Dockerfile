FROM python:3.9.12-slim-buster
MAINTAINER wangwentao "37362762@qq.com"

# Set the working directory to /app
WORKDIR /mysit

# Copy the current directory contents into the container at /mysit
COPY . /mysit

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8880

CMD ["python", "main.py"]
