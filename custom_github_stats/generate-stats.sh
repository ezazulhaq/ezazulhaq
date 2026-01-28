#!/bin/bash

# Script to generate GitHub stats SVGs
# Usage: ./generate-stats.sh <YOUR_GITHUB_TOKEN>

if [ -z "$1" ]; then
    echo "Error: GitHub token not provided"
    echo "Usage: ./generate-stats.sh <YOUR_GITHUB_TOKEN>"
    echo ""
    echo "Or set GITHUB_TOKEN environment variable and run without arguments"
    echo "Usage: GITHUB_TOKEN=your_token ./generate-stats.sh"
    exit 1
fi

TOKEN=${1:-$GITHUB_TOKEN}

cd "$(dirname "$0")"

echo "Generating GitHub stats SVGs..."
python3 main.py --username ezazulhaq --token "$TOKEN"

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ SVG files generated successfully!"
    echo "  - github-streak-stats.svg"
    echo "  - github-language-stats.svg"
    echo ""
    echo "Files are located in the parent directory (repository root)"
else
    echo ""
    echo "✗ Failed to generate SVG files"
    exit 1
fi
