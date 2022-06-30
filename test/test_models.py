import itertools

import pytest


def pytest_generate_tests(metafunc):
    argnames = metafunc.fixturenames[:-1]

    skipped_models = get_skipped_models(metafunc)
    all_models = set(metafunc.cls.models)
    argvalues = [
        pytest.param(
            *[model for _ in range(len(argnames))],
            marks=pytest.mark.skip if model in skipped_models else (),
        )
        for model in all_models
    ]
    metafunc.parametrize(argnames, argvalues, indirect=True, ids=all_models, scope="class")


def get_skipped_models(metafunc):
    marks = getattr(metafunc.function, "pytestmark", [])
    skip_marks = [list(mark.args) for mark in marks if mark.name == "skip_models"]
    skipped_models = set(itertools.chain.from_iterable(skip_marks))
    return skipped_models


class TestSampleWithScenarios:
    models = ["abb", "b", "c"]

    @pytest.mark.skip_models("b", "z")
    def test_model_step1(self, short_list, long_list):
        new_list = short_list + ["z"]
        assert new_list == long_list

    def test_model_step2(self, short_list, long_list):
        new_list = short_list + ["z"]
        assert new_list == long_list
