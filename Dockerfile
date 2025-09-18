# Use the official Python runtime as a parent image
# You can change the version tag (e.g., 3.9, 3.10, 3.11-bookworm)
FROM python:3.11-slim-bookworm

# Create a non-root user and group with the same IDs as my host's user
ARG UID
ARG GID
ARG USR

RUN groupadd -g $GID $USR && \
    useradd -m -u $UID -g $GID -s /bin/bash $USR

# Set the working directory in the container
# Ensure it is owned by the new user
WORKDIR /app
RUN chown $USR:$USR /app

# Copy & install the requirements first for better layering caching
COPY --chown=$USR:$USR requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the App code, maintain ownership
COPY --chown=$USR:$USR . .

# Now switch to the new user
USER $USR

# Define environment variable to ensure Python output is sent straight to terminal
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
# CMD ["python", "app.py"]
# Note: We will override this command when we run interactively.