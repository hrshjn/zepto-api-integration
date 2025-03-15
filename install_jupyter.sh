#!/bin/bash

echo "===== Installing Jupyter Notebook ====="
echo ""
echo "This script will install Jupyter Notebook using pip."
echo ""

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "Error: pip is not installed. Please install pip first."
    echo "You can install pip by running: 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py'"
    exit 1
fi

# Ask for confirmation
read -p "Do you want to install Jupyter Notebook? (y/n) " CONFIRM

if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    # Install Jupyter
    echo "Installing Jupyter Notebook..."
    pip install jupyter notebook
    
    echo ""
    echo "Installation complete. You can now run Jupyter Notebook with:"
    echo "jupyter notebook"
    echo ""
    echo "To run the Zepto test notebook specifically:"
    echo "cd mcp/zepto && jupyter notebook zepto_test.ipynb"
else
    echo "Installation cancelled."
fi

echo "===== End of Installation =====" 