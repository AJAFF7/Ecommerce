# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE ecommerce.settings

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code/
COPY requirements.txt /code/

# Install dependencies
RUN pip install -r requirements.txt -U

# Copy the current directory contents into the container at /code/
COPY . /code/

# Expose port
EXPOSE 8000

# Define the default command
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
