#!/bin/bash

# Instructions for creating a GitHub repository and pushing the code
echo "===== GitHub Repository Setup Instructions ====="
echo ""
echo "1. Go to https://github.com/new"
echo "2. Enter 'zepto-api-integration' as the Repository name"
echo "3. Add a description: 'Python integration with Zepto API using FastMCP'"
echo "4. Choose 'Public' or 'Private' visibility as preferred"
echo "5. Click 'Create repository'"
echo ""
echo "After creating the repository, run the following commands (replace YOUR_GITHUB_USERNAME with your actual GitHub username):"
echo ""
echo "git remote add origin https://github.com/YOUR_GITHUB_USERNAME/zepto-api-integration.git"
echo "git branch -M main"
echo "git push -u origin main"
echo ""
echo "For example, if your GitHub username is 'harshjain', the command would be:"
echo "git remote add origin https://github.com/harshjain/zepto-api-integration.git"
echo ""
echo "===== End of Instructions ====="

# Make the script executable
chmod +x create_github_repo.sh 