import sys
import os
import json
import time
import requests

# Function to test different payload and header combinations
def test_verify_otp(mobile_number, otp):
    """
    Tests different combinations of payload formats and headers to debug the RequestContentLengthMismatchError.
    """
    url = "https://api.zeptonow.com/api/v1/user/customer/verify-otp"

    # Method 1: Using json.dumps() (current approach)
    payload_json_dumps = json.dumps({
        "mobileNumber": mobile_number,
        "otpToken": otp
    })
    
    # Method 2: Using string concatenation (like request_otp)
    payload_string = "{\"mobileNumber\":\"" + mobile_number + "\",\"otpToken\":\"" + otp + "\"}"
    
    # Log both payload methods for comparison
    print("\n=== PAYLOAD COMPARISON ===")
    print(f"Method 1 (json.dumps): {payload_json_dumps}")
    print(f"Method 1 Length: {len(payload_json_dumps)} chars, {len(payload_json_dumps.encode('utf-8'))} bytes")
    print(f"Method 2 (string): {payload_string}")
    print(f"Method 2 Length: {len(payload_string)} chars, {len(payload_string.encode('utf-8'))} bytes")
    
    # Current headers
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
    
    # Print header comparison with request_otp
    print("\n=== HEADER COMPARISON ===")
    print("verify_otp content-type:", headers.get('content-type'))
    print("should be like request_otp: application/json; charset=UTF-8")
    
    # Create modified headers with charset
    headers_with_charset = headers.copy()
    headers_with_charset['content-type'] = 'application/json; charset=UTF-8'
    
    # Test both payload methods
    print("\n=== TEST 1: Current approach (json.dumps + original headers) ===")
    response1 = requests.request("POST", url, headers=headers, data=payload_json_dumps)
    print(f"Status Code: {response1.status_code}")
    print(f"Response: {response1.text}")
    
    print("\n=== TEST 2: String concatenation + original headers ===")
    response2 = requests.request("POST", url, headers=headers, data=payload_string)
    print(f"Status Code: {response2.status_code}")
    print(f"Response: {response2.text}")
    
    print("\n=== TEST 3: Current approach + headers with charset ===")
    response3 = requests.request("POST", url, headers=headers_with_charset, data=payload_json_dumps)
    print(f"Status Code: {response3.status_code}")
    print(f"Response: {response3.text}")
    
    print("\n=== TEST 4: String concatenation + headers with charset ===")
    response4 = requests.request("POST", url, headers=headers_with_charset, data=payload_string)
    print(f"Status Code: {response4.status_code}")
    print(f"Response: {response4.text}")
    
    # Method 5: Using json parameter instead of data
    print("\n=== TEST 5: Using json parameter (no manual serialization) ===")
    response5 = requests.request("POST", url, headers=headers, json={"mobileNumber": mobile_number, "otpToken": otp})
    print(f"Status Code: {response5.status_code}")
    print(f"Response: {response5.text}")
    
    # Report best method
    print("\n=== CONCLUSION ===")
    results = [
        ("Method 1 (json.dumps + original headers)", response1.status_code),
        ("Method 2 (string concat + original headers)", response2.status_code),
        ("Method 3 (json.dumps + charset headers)", response3.status_code),
        ("Method 4 (string concat + charset headers)", response4.status_code),
        ("Method 5 (json parameter)", response5.status_code)
    ]
    
    for method, status in results:
        print(f"{method}: Status {status}")
    
    # Identify best method
    best_method = None
    best_response = None
    
    for i, (method, status) in enumerate(results):
        if status == 200:
            best_method = method
            best_response = [response1, response2, response3, response4, response5][i]
            break
    
    if best_method:
        print(f"\nBest method: {best_method}")
        print(f"Response: {best_response.text}")
        return best_response
    else:
        print("\nNo method worked successfully (status code 200)")
        return response1  # Return first response as default

if __name__ == "__main__":
    print("\n=== ZEPTO OTP VERIFICATION DEBUG TEST ===")
    
    # Ask for the phone number
    mobile_number = input("Enter your phone number (without country code): ")
    
    # Ask for the OTP
    otp = input("Enter the OTP you received: ")
    
    # Test verify_otp function with different approaches
    result = test_verify_otp(mobile_number, otp) 