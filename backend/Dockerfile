# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app/backend

# Copy the Flask application code into the container
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port on which the Flask application runs
EXPOSE 5000

# Define the command to run the Flask application when the container starts
CMD [ "python", "main.py" ]
