#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run tests in parallel
pytest tests/test_main.py &

# Run main script
python src/main.py
