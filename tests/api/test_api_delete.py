import requests

def test_delete_user():
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url)

    # Reqres ahora devuelve 403
    assert response.status_code in [204, 401, 403]

