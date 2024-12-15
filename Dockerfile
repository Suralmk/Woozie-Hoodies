FROM python:3.11-slim-bullseye

# Install system dependencies required by WeasyPrint
RUN apt-get update && apt-get install -y \
    gcc \
    libglib2.0-0 \
    libpango1.0-0 \
    libcairo2 \
    libgirepository-1.0-1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /woozieapp

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Make sure all dependencies are installed
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
