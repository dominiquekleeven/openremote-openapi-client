#!/usr/bin/env python3
"""
OpenRemote REST Client Assets Example

Fill in your credentials below and run:
    python assets-example.py
"""

import sys
from pathlib import Path


from or_rest_client import AuthenticatedApiClient, AssetApi, AssetQuery


def main():
    realm = "master" # The realm to use
    
    BASE_URL = f"http://localhost:8080/api/{realm}"
    KEYCLOAK_URL = "http://localhost:8081/auth"
    CLIENT_ID = "serviceuser"
    CLIENT_SECRET = "secret"
    REALM = realm

    print("OpenRemote REST Client Assets Example")

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
        
        # Create asset API instance
        asset_api = AssetApi(api_client)

        # Query assets with basic info
        print("Querying assets...")
        query = AssetQuery(limit=10)
        query_response = asset_api.query_assets(asset_query=query)
        print(f"Query response: {query_response}")

        print("Assets example completed successfully!")
        return True

    except Exception as e:
        print(f"Assets example failed: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
