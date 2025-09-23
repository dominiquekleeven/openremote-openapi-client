#!/usr/bin/env python3
"""
OpenRemote REST Client Health Check Example

Fill in your credentials below and run:
    python healthcheck-example.py
"""

import sys
import logging
from pathlib import Path

from or_rest_client import AuthenticatedApiClient, StatusApi, Configuration

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)


def main():
    realm = "master" # The realm to use
    
    BASE_URL = f"http://localhost:8080/api/{realm}"
    KEYCLOAK_URL = "http://localhost:8081/auth"
    CLIENT_ID = "serviceuser"
    CLIENT_SECRET = "secret"
    REALM = realm

    print("OpenRemote REST Client Health Check")

    try:
        # Create authenticated API client with Keycloak
        api_client = AuthenticatedApiClient(
            base_url=BASE_URL,
            keycloak_url=KEYCLOAK_URL,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            realm=REALM,
            timeout=30.0
        )
        
        # Check authentication
        print("Checking authentication...")
        if not api_client.is_authenticated:
            print("Authentication failed")
            return False
        
        print(f"Authentication successful (expires in {api_client.token_expires_in}s)")
        
        # Create status API instance
        status_api = StatusApi(api_client)

        # Perform health check
        print("Performing health check...")
        health_response = status_api.get_health_status()
        print(f"Health check passed: {health_response}")

        # Get system info
        print("Getting system info...")
        info_response = status_api.get_info()
        print(f"System info: {info_response}")

        print("Health check completed successfully!")
        return True

    except Exception as e:
        print(f"Health check failed: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
