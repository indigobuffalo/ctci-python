import pytest

from hamcrest import assert_that, equal_to

from src.chapters.one.is_unique import is_unique

class TestIsUnique:

    @pytest.mark.parametrize("input, expected", [("abc", True), ("abcc", False), ("abcdedf", False)])
    def test_is_unique(self, input, expected):
        assert_that(is_unique(input), equal_to(expected))

