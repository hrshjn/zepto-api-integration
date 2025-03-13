import requests
import sys
import os
import time
import json
from fastmcp import FastMCP

##############################################################################
# 1) CREATE MCP INSTANCE & GLOBAL SESSIONS
##############################################################################

mcp = FastMCP("Zepto MCP Server (API)")

# We'll store a global session for API requests after auth
SESSION = requests.Session()

# Base URLs
ZEPTO_BASE_URL = "https://api.zeptonow.com"
ZEPTO_WEB_URL = "https://www.zeptonow.com"

# API Endpoints 
REQUEST_OTP_URL = f"{ZEPTO_BASE_URL}/api/v1/user/customer/send-otp-sms/"
VERIFY_OTP_URL = f"{ZEPTO_BASE_URL}/api/v1/user/customer/verify-otp"
REFRESH_URL = f"{ZEPTO_BASE_URL}/api/v1/user/customer/refresh"
GET_ORDERS_URL = f"{ZEPTO_BASE_URL}/api/v2/order/?page_number=1"

# Complete headers for requests
DEFAULT_HEADERS = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'access-control-allow-credentials': 'true',
    'access-control-allow-methods': 'GET, POST, OPTIONS',
    'access-control-allow-origin': '*',
    'app_sub_platform': 'WEB',
    'app_version': '12.56.0',
    'appversion': '12.56.0',
    'auth_revamp_flow': 'v2',
    'bundleversion': 'v1',
    'compatible_components': 'CONVENIENCE_FEE,NEW_FEE_STRUCTURE,NEW_BILL_INFO,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,SUPERSTORE_V1,MANUALLY_APPLIED_DELIVERY_FEE_RECEIVABLE,MARKETPLACE_REPLACEMENT,ZEPTO_PASS,ZEPTO_PASS:1,ZEPTO_PASS:2,ZEPTO_PASS_RENEWAL,CART_REDESIGN_ENABLED,SHIPMENT_WIDGETIZATION_ENABLED,TABBED_CAROUSEL_V2,24X7_ENABLED_V1,PROMO_CASH:0,HOMEPAGE_V2,SUPER_SAVER:1,NO_PLATFORM_CHECK_ENABLED_V2,HP_V4_FEED,GIFTING_ENABLED,OFSE,WIDGET_BASED_ETA,',
    'content-type': 'application/json; charset=UTF-8',
    'device_id': '9b323a31-644f-4b50-8788-b0be4483a8e6',
    'deviceid': '9b323a31-644f-4b50-8788-b0be4483a8e6',
    'deviceuid': '',
    'marketplace_type': 'ZEPTO_NOW',
    'origin': 'https://www.zeptonow.com',
    'platform': 'WEB',
    'priority': 'u=1, i',
    'referer': 'https://www.zeptonow.com/',
    'request_id': '9a7c4f5c-b282-46a7-8c46-87efe938b5e5',
    'requestid': '9a7c4f5c-b282-46a7-8c46-87efe938b5e5',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'session_id': 'd54bded5-810d-4430-91d7-aebe8f1dd7ae',
    'sessionid': 'd54bded5-810d-4430-91d7-aebe8f1dd7ae',
    'store_etas': '{"fa5e892d-65d7-4da6-9bde-e1f22deb7b6f":-1}',
    'store_id': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
    'store_ids': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
    'storeid': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
    'systemversion': '',
    'tenant': 'ZEPTO',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36',
    'x-request-intercepted': 'true',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'o430DHseVJB9DXdA8lqqL:I_7KDxAD37UWoD9I7c70vjiy7V4.Cd1Rju3YrEakW6QKP7z21ogML0bDNHSeTtzMzzg+Lzw',
    'Cookie': '_gcl_au=1.1.1343294330.1733745096; _ga=GA1.1.648046305.1733745096; _fbp=fb.1.1733745096521.40454641945162008; _ga_37QQVCR1ZS=GS1.1.1733745113.1.0.1733745113.60.0.0; mp_dcc8757645c1c32f4481b555710c7039_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A19572856216e12-0edb31b1590b14-1c525636-16a7f0-19572856216e12%22%2C%22%24device_id%22%3A%20%2219572856216e12-0edb31b1590b14-1c525636-16a7f0-19572856216e12%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.zeptonow.com%2Faccount%22%2C%22%24initial_referring_domain%22%3A%20%22www.zeptonow.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.zeptonow.com%2Faccount%22%2C%22%24initial_referring_domain%22%3A%20%22www.zeptonow.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_52LKG2B3L1=GS1.1.1741383050.28.1.1741383122.53.0.686375875'
}

##############################################################################
# 2) MCP TOOL: REQUEST OTP
##############################################################################
@mcp.tool()
def request_otp(mobile_number: str) -> dict:
    """
    Requests OTP using Zepto's API.
    
    Args:
        mobile_number: The phone number (without country code)
    """
    try:
        # Clean the phone number
        url = "https://api.zeptonow.com/api/v1/user/customer/send-otp-sms/"

        payload = "{\"mobileNumber\":\"" + mobile_number + "\"}"
        headers = {
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'access-control-allow-credentials': 'true',
        'access-control-allow-methods': 'GET, POST, OPTIONS',
        'access-control-allow-origin': '*',
        'app_sub_platform': 'WEB',
        'app_version': '12.56.0',
        'appversion': '12.56.0',
        'auth_revamp_flow': 'v2',
        'bundleversion': 'v1',
        'compatible_components': 'CONVENIENCE_FEE,NEW_FEE_STRUCTURE,NEW_BILL_INFO,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,SUPERSTORE_V1,MANUALLY_APPLIED_DELIVERY_FEE_RECEIVABLE,MARKETPLACE_REPLACEMENT,ZEPTO_PASS,ZEPTO_PASS:1,ZEPTO_PASS:2,ZEPTO_PASS_RENEWAL,CART_REDESIGN_ENABLED,SHIPMENT_WIDGETIZATION_ENABLED,TABBED_CAROUSEL_V2,24X7_ENABLED_V1,PROMO_CASH:0,HOMEPAGE_V2,SUPER_SAVER:1,NO_PLATFORM_CHECK_ENABLED_V2,HP_V4_FEED,GIFTING_ENABLED,OFSE,WIDGET_BASED_ETA,',
        'content-type': 'application/json; charset=UTF-8',
        'device_id': '9b323a31-644f-4b50-8788-b0be4483a8e6',
        'deviceid': '9b323a31-644f-4b50-8788-b0be4483a8e6',
        'deviceuid': '',
        'marketplace_type': 'ZEPTO_NOW',
        'origin': 'https://www.zeptonow.com',
        'platform': 'WEB',
        'priority': 'u=1, i',
        'referer': 'https://www.zeptonow.com/',
        'request_id': '9a7c4f5c-b282-46a7-8c46-87efe938b5e5',
        'requestid': '9a7c4f5c-b282-46a7-8c46-87efe938b5e5',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'session_id': 'd54bded5-810d-4430-91d7-aebe8f1dd7ae',
        'sessionid': 'd54bded5-810d-4430-91d7-aebe8f1dd7ae',
        'store_etas': '{"fa5e892d-65d7-4da6-9bde-e1f22deb7b6f":-1}',
        'store_id': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
        'store_ids': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
        'storeid': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
        'systemversion': '',
        'tenant': 'ZEPTO',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36',
        'x-request-intercepted': 'true',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'o430DHseVJB9DXdA8lqqL:I_7KDxAD37UWoD9I7c70vjiy7V4.Cd1Rju3YrEakW6QKP7z21ogML0bDNHSeTtzMzzg+Lzw',
        'Cookie': '_gcl_au=1.1.1343294330.1733745096; _ga=GA1.1.648046305.1733745096; _fbp=fb.1.1733745096521.40454641945162008; _ga_37QQVCR1ZS=GS1.1.1733745113.1.0.1733745113.60.0.0; mp_dcc8757645c1c32f4481b555710c7039_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A19572856216e12-0edb31b1590b14-1c525636-16a7f0-19572856216e12%22%2C%22%24device_id%22%3A%20%2219572856216e12-0edb31b1590b14-1c525636-16a7f0-19572856216e12%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.zeptonow.com%2Faccount%22%2C%22%24initial_referring_domain%22%3A%20%22www.zeptonow.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.zeptonow.com%2Faccount%22%2C%22%24initial_referring_domain%22%3A%20%22www.zeptonow.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_52LKG2B3L1=GS1.1.1741383050.28.1.1741383122.53.0.686375875'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    except Exception as e:
        print(f"\nEXCEPTION DETAILS:", file=sys.stderr)
        print(f"Error Type: {type(e).__name__}", file=sys.stderr)
        print(f"Error Message: {str(e)}", file=sys.stderr)
        print(f"Stack Trace:", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
            
        return {
            "error": {
                "exception": str(e),
                "message": "An error occurred while sending the OTP request"
            }
        }
    

##############################################################################
# 3) MCP TOOL: VERIFY OTP
##############################################################################
@mcp.tool()
def verify_otp(mobile_number: str, otp: str) -> dict:
    """
    Verifies OTP using Zepto's API.
    Captures authentication tokens for future API requests.
    
    Args:
        mobile_number: The phone number (without country code)
        otp: The one-time password received
    """
    url = "https://api.zeptonow.com/api/v1/user/customer/verify-otp"

    payload = json.dumps({
    "mobileNumber": mobile_number,
    "otpToken": otp
    })
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'app_sub_platform': 'WEB',
    'app_version': '12.59.0',
    'appversion': '12.59.0',
    'auth_revamp_flow': 'v2',
    'compatible_components': ',NEW_FEE_STRUCTURE,NEW_BILL_INFO,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,SUPERSTORE_V1,MANUALLY_APPLIED_DELIVERY_FEE_RECEIVABLE,MARKETPLACE_REPLACEMENT,ZEPTO_PASS,ZEPTO_PASS:1,ZEPTO_PASS:2,ZEPTO_PASS_RENEWAL,CART_REDESIGN_ENABLED,SHIPMENT_WIDGETIZATION_ENABLED,TABBED_CAROUSEL_V2,24X7_ENABLED_V1,PROMO_CASH:0,HOMEPAGE_V2,SUPER_SAVER:1,NO_PLATFORM_CHECK_ENABLED_V2,HP_V4_FEED,GIFTING_ENABLED,OFSE,WIDGET_BASED_ETA,',
    'content-type': 'application/json',
    'device_id': '0332ee85-4fa4-4f53-a61e-64b01bb1b628',
    'deviceid': '0332ee85-4fa4-4f53-a61e-64b01bb1b628',
    'marketplace_type': 'ZEPTO_NOW',
    'origin': 'https://www.zeptonow.com',
    'platform': 'WEB',
    'priority': 'u=1, i',
    'referer': 'https://www.zeptonow.com/',
    'request_id': 'a1bebc28-3d98-4256-a40f-a6c8ead6e565',
    'requestid': 'a1bebc28-3d98-4256-a40f-a6c8ead6e565',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'session_id': 'f55fb1ac-d440-4938-bed2-b8d3f3725445',
    'sessionid': 'f55fb1ac-d440-4938-bed2-b8d3f3725445',
    'store_etas': '{"fa5e892d-65d7-4da6-9bde-e1f22deb7b6f":-1}',
    'store_id': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
    'store_ids': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
    'storeid': 'fa5e892d-65d7-4da6-9bde-e1f22deb7b6f',
    'tenant': 'ZEPTO',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36',
    'x-request-intercepted': 'true',
    'x-xsrf-token': 'Gl_gwNfZDDZybVDRvXl34:FpV0ylyRKYRiksIFlKmKLYGRoNo.3oFuY6oTPaGRwWZDTevP0jbzCxgs2hihIsJp9ht6lys',
    'Cookie': '_ga=GA1.1.648046305.1733745096; _fbp=fb.1.1733745096521.40454641945162008; _ga_37QQVCR1ZS=GS1.1.1733745113.1.0.1733745113.60.0.0; _gcl_au=1.1.1465585140.1741852979; mp_dcc8757645c1c32f4481b555710c7039_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A1958e88c3c119707-065ce2025d6816-42015519-5f3c0-1958e88c3c119707%22%2C%22%24device_id%22%3A%20%221958e88c3c119707-065ce2025d6816-42015519-5f3c0-1958e88c3c119707%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.zeptonow.com%2Faccount%22%2C%22%24initial_referring_domain%22%3A%20%22www.zeptonow.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.zeptonow.com%2Faccount%22%2C%22%24initial_referring_domain%22%3A%20%22www.zeptonow.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_52LKG2B3L1=GS1.1.1741852966.52.1.1741853096.39.0.1179499877; accessToken=eyJhbGciOiJIUzUxMiJ9.eyJ2ZXJzaW9uIjoxLCJzdWIiOiIyNjY0ZjY4Mi0yMGUxLTQ1Y2QtOTgyMy0zOTliZGVjNWUxNWQiLCJpYXQiOjE3NDE4NTMxNzcsImV4cCI6MTc0MTkzOTU3N30.JB14RZq0nzy4hz0GLqpiTbVxOZ-TRQVkXSN46n7ZA9empDT4WmfTrNsUgPSLk5hb_Utbyt5LFy3y01z1PqZ4RA; isAuth=true; refreshToken=55a7535b-d2d2-4b7e-9b18-63b5b222e6fe'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    return {
        "accessToken": response.json()
    }

##############################################################################
# 4) MCP TOOL: REFRESH TOKEN
##############################################################################
@mcp.tool()
def refresh_zepto_token() -> dict:
    """
    Uses the refreshToken to get a new accessToken.
    """
    pass  # To be implemented

##############################################################################
# 5) MCP RESOURCE: GET ORDERS (AUTO REFRESH IF EXPIRED)
##############################################################################
@mcp.resource("zepto://orders")
def get_orders() -> dict:
    """
    Fetch order history from Zepto. 
    If we get a 401 or 403, we automatically call refresh_zepto_token() and retry.
    Handles rate limiting (429) with exponential backoff.
    """
    pass  # To be implemented

##############################################################################
# 6) RUN MCP SERVER
##############################################################################
if __name__ == "__main__":
    # Test request_otp function
    print("Testing request_otp function...")
    
    # Use the payload as a dict
    mobile_number = "8850842341"
    payload = {"mobileNumber": mobile_number}
    
    # Make direct request using requests.post
    response = requests.post(
        url=REQUEST_OTP_URL,
        json=payload,
        headers=DEFAULT_HEADERS
    )
    
    print("\n=== DIRECT REQUEST RESULT ===")
    print(f"Status Code: {response.status_code}")
    print(response.text)
    print("=== END DIRECT REQUEST RESULT ===\n")
    
    # Also test using the tool function
    result = request_otp(mobile_number)
    print("\n=== TOOL FUNCTION RESULT ===")
    print(json.dumps(result, indent=2))
    print("=== END TOOL FUNCTION RESULT ===\n")