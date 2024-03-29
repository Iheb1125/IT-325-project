# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose a port (if your application listens on a specific port)
EXPOSE 5000

# Command to run your application
CMD ["python", "all.py"]
