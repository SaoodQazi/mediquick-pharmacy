from app import create_app


def test_search_returns_matching_medicine():
    response = create_app().test_client().get("/medicines?q=para")
    assert [m["name"] for m in response.get_json()] == ["Paracetamol 500mg"]


def test_search_with_no_match_returns_empty_list():
    response = create_app().test_client().get("/medicines?q=zzz")
    assert response.get_json() == []
