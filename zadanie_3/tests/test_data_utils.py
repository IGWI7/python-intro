from my_awesome_lib.data_utils import filter_data

def test_filter_data_basic():
    data = [
        {"name": "Alice", "role": "admin"},
        {"name": "Bob", "role": "user"},
        {"name": "Eve", "role": "admin"},
    ]
    result = filter_data(data, "role", "admin")
    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["name"] == "Eve"
