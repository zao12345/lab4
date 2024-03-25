# Use an official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into to the container
COPY requirements.txt .

# Install npm dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that your app runs on
EXPOSE 5000

# Define the command to run your app
CMD [ "python", "server.py" ]

