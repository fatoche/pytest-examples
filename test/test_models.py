import itertools

import pytest


def pytest_generate_tests(metafunc):
    argnames = metafunc.fixturenames[:-1]
    argvalues = [
        [model for _ in range(len(argnames))]
        for model in metafunc.cls.models
    ]
    metafunc.parametrize(argnames, argvalues, indirect=True, ids=metafunc.cls.models, scope="class")


class TestSampleWithScenarios:
    models = ["abb", "b", "c"]

    def test_model_step1(self, short_list, long_list):
        new_list = short_list + ["z"]
        assert new_list == long_list

    def test_model_step2(self, short_list, long_list):
        new_list = short_list + ["z"]
        assert new_list == long_list
