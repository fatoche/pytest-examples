import pytest


@pytest.fixture()
def short_list(request):
    return [request.param for _ in range(3)]


@pytest.fixture()
def long_list(request):
    return [request.param for _ in range(3)] + ["z"]
