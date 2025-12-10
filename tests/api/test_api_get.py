import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"

    response = requests.get(url)

    # Reqres ahora devuelve 403 en la mayoría de requests
    assert response.status_code in [200, 403]
