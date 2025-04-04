# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Prevents Python from writing pyc files to disc and enables buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run"]
