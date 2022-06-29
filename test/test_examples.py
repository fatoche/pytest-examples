import pytest


@pytest.mark.parametrize(
    ["short_list", "long_list"],
    [
        pytest.param("abb", "abb"),
        pytest.param("b", "b", marks=pytest.mark.skip),
        pytest.param("c", "c"),
    ],
    indirect=True
)
def test_model_step(short_list, long_list):
    new_list = short_list + ["z"]
    assert new_list == long_list
