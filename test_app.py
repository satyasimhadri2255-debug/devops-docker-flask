import requests

def test_homepage_returns_message():
    r = requests.get("http://localhost:5000/")
    assert r.status_code == 200
    assert "DevOps" in r.text  # checks your homepage message contains this word

def test_health_endpoint():
    r = requests.get("http://localhost:5000/health")
    assert r.status_code == 200
    assert r.text.strip() == "OK"
