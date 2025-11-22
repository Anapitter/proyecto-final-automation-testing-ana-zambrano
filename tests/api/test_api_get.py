import requests

def test_get_users():
    # Endpoint público
    url = "https://reqres.in/api/users?page=2"
    headers = {"x-api-key": "regres-free-v1"}

    # Executing GET
    response = requests.get(url, headers=headers)

    # Validación de estado
    assert response.status_code == 200

    # Body
    data = response.json()

    # Validaciones de estructura
    assert "data" in data
    assert len(data["data"]) > 0
    assert len(data["data"]) == 6  # Reqres siempre devuelve 6 items en page=2
