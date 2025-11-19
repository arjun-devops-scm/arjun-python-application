# Use a lightweight official Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on (update if different)
EXPOSE 5000

# Environment variable (optional but useful)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the app
CMD ["flask", "run"]
