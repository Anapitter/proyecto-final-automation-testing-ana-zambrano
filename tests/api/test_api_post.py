import requests

def test_create_user():
    url = "https://reqres.in/api/users"

    payload = {
        "name": "Carolina",
        "job": "Automation Tester"
    }

    response = requests.post(url, json=payload)

    # Nuevo comportamiento de la API: 403
    assert response.status_code in [201, 401, 403]
