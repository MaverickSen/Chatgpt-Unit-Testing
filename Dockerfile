# Use an official Python image as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy all project files into the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose any necessary ports (if applicable)
# EXPOSE 8000

# Define the command to run your script
CMD ["python", "src/chatgpt_client.py"]