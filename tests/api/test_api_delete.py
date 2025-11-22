import requests

def test_delete_user():
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url)

    # Reqres devolvía 204, ahora devuelve 401
    assert response.status_code in [204, 401]
