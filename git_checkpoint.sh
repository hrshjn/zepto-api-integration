#!/bin/bash

# Check if a commit message was provided
if [ $# -eq 0 ]; then
    echo "Error: No commit message provided."
    echo "Usage: ./git_checkpoint.sh \"Your commit message\""
    exit 1
fi

# Get the commit message from the first argument
COMMIT_MESSAGE="$1"

# Display the current Git status
echo "===== Current Git Status ====="
git status
echo "============================="

# Ask for confirmation
read -p "Do you want to commit and push all changes with the message: \"$COMMIT_MESSAGE\"? (y/n) " CONFIRM

if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    # Add all changes
    git add .
    
    # Commit with the provided message
    git commit -m "$COMMIT_MESSAGE"
    
    # Push to the remote repository
    git push
    
    echo "===== Checkpoint Complete ====="
    echo "All changes have been committed and pushed with the message:"
    echo "\"$COMMIT_MESSAGE\""
else
    echo "Operation cancelled."
fi 