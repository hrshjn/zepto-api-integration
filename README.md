# Zepto API Integration

A Python integration with Zepto's API using FastMCP for building automation tools.

## Overview

This project provides a set of tools to interact with Zepto's API, allowing you to:

- Request OTP for authentication
- Verify OTP and get authentication tokens
- Refresh authentication tokens
- Retrieve order history

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hrshjn/zepto-api-integration.git
cd zepto-api-integration
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Authentication

The authentication flow involves two steps:

1. Request an OTP:
```python
from mcp.zepto.server import request_otp

# Replace with your actual phone number
result = request_otp("your_phone_number")
print(result)
```

2. Verify the OTP:
```python
from mcp.zepto.server import verify_otp

# Replace with your actual phone number and the OTP you received
result = verify_otp("your_phone_number", "your_otp")
print(result)
```

### Testing

To test the API integration:

```bash
python mcp/zepto/server.py
```

**Note:** The code uses a placeholder phone number (`1234567890`) for testing. Replace it with your actual phone number when testing the functionality.

## Security Note

- Never commit your actual phone number or authentication tokens to the repository
- The placeholder phone number in the code is for demonstration purposes only
- Always use environment variables or secure configuration files to store sensitive information

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 