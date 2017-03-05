import pytest
from grappa import should, expect
from grappa.operators.none import NoneOperator


def test_should_none():
    None | should.be.none

    with pytest.raises(AssertionError):
        False | should.be.none

    with pytest.raises(AssertionError):
        None | should.be.none

    with pytest.raises(AssertionError):
        'foo' | should.be.none

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.be.none


def test_expect_none():
    None | expect.be.none

    with pytest.raises(AssertionError):
        False | expect.be.none

    with pytest.raises(AssertionError):
        None | expect.be.none

    with pytest.raises(AssertionError):
        'foo' | expect.be.none

    with pytest.raises(AssertionError):
        [1, 2, 3] | expect.be.none


def test_none_operator(ctx):
    assert NoneOperator(ctx).match(True) == (True, [])
    assert NoneOperator(ctx).match(False) == (False, [])

    assert NoneOperator(ctx).match(0) == (False,
                                          ['subject is not a bool type'])