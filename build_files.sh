#!/bin/bash

# Build the project
echo "Building the project..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

echo "Build completed!"
