"""Placeholder tests so the CI pipeline has something to run."""


def test_sanity():
    assert 1 + 1 == 2


def test_string():
    assert "ci".upper() == "CI"


class TestPlaceholder:
    def test_list_membership(self):
        assert 3 in [1, 2, 3]

    def test_dict_lookup(self):
        data = {"env": "ci"}
        assert data.get("env") == "ci"
