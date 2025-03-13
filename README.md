# Zepto API Integration

This repository contains tools for interacting with the Zepto API using Python. It's built using the FastMCP framework to create a structured API client.

## Features

- Request OTP for authentication
- Verify OTP and obtain access tokens
- Refresh authentication tokens
- Retrieve order history

## Project Structure

```
mcp/
  └── zepto/
      ├── server.py       # Main API integration code
      └── zepto_test.ipynb # Jupyter notebook for testing
```

## Getting Started

### Prerequisites

- Python 3.6+
- Required packages: `requests`, `fastmcp`

### Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install requests fastmcp
   ```

### Usage

To run the server:

```bash
python mcp/zepto/server.py
```

To test the API in a Jupyter notebook:

```bash
cd mcp/zepto
jupyter notebook zepto_test.ipynb
```

## API Functions

### Request OTP

```python
request_otp(mobile_number: str) -> dict
```

Sends an OTP to the provided mobile number.

### Verify OTP

```python
verify_otp(mobile_number: str, otp: str) -> dict
```

Verifies the OTP and returns authentication tokens.

### Refresh Token

```python
refresh_zepto_token() -> dict
```

Refreshes the authentication token when it expires.

### Get Orders

```python
get_orders() -> dict
```

Retrieves the order history from Zepto.

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 