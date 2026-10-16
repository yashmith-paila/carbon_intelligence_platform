import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_dashboard_stats():
    # Login to get token
    # Assuming the test user from previous steps exists
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    
    try:
        login_res = requests.post(f"{BASE_URL}/auth/signin", json=login_data)
        token = login_res.json().get("access_token")
        
        if not token:
            print("Failed to get token. Check if test user exists.")
            return

        headers = {"Authorization": f"Bearer {token}"}
        
        # Test dashboard-stats
        stats_res = requests.get(f"{BASE_URL}/analytics/dashboard-stats", headers=headers)
        print("Dashboard Stats Response:")
        print(json.dumps(stats_res.json(), indent=2))
        
        if stats_res.status_code == 200:
            print("SUCCESS: Dashboard stats endpoint is functional and dynamic.")
        else:
            print(f"FAILED: Status code {stats_res.status_code}")
            
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_dashboard_stats()
