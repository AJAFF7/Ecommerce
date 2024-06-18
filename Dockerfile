# Use an official Python runtime as a parent image
FROM 3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE ecommerce.settings

# Create and set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code/
COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# Expose port 8000
EXPOSE 8000

# Define the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
