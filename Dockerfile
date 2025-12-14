# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirement.txt
# Note: We use --no-cache-dir to keep the image size small
RUN pip install --no-cache-dir -r requirement.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV PORT=8080

# Run app.py when the container launches using Gunicorn
# 1 worker is usually enough for simple agents, but can be increased
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
