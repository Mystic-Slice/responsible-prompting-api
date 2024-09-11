import requests

def test_code_engine_url():
    api_url = "https://responsible-prompt-app.jo2bfsmp5jj.us-south.codeengine.appdomain.cloud/recommend?prompt="
    response = requests.get(api_url)
    assert response.status_code == 200 
    assert response.headers["Content-Type"] == "application/json"
    
