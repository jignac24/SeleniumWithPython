import requests
import json


class Test_RestAPI:
    BaseURL = "https://gorest.co.in/public/v2"
    headers = {"Authorization": "Bearer 1cc92ca6ecec7720d344d23b5c12ddba35e2ded139ad8b11d28b52eeef32a51a"}

    def test_Get_allUsers(self):
        response = requests.get(url=self.BaseURL + "/users", headers=self.headers)
        assert response.status_code == 200
        res_data = json.dumps(response.json(), indent=4)
        print(res_data)

    def test_Get_User(self):
        response = requests.get(url=self.BaseURL + "/users/7028296", headers=self.headers)
        assert response.status_code == 200
        res_data = json.dumps(response.json(), indent=4)
        print(res_data)

    def test_post_user(self):
        payload = {
            "name": "test",
            "gender": "female",
            "email": "test5py@gmail.com",
            "status": "active"
        }
        response = requests.post(url=self.BaseURL + "/users", headers=self.headers, json=payload)
        assert response.status_code == 201
        jsonData = response.json()
        res_data = json.dumps(jsonData, indent=4)
        user_id = jsonData["id"]
        print(res_data)
        url = f"/users/{user_id}"
        delRes = requests.delete(url=self.BaseURL + url, headers=self.headers, json={})
        assert delRes.status_code == 204
