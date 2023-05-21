import numpy as np

from glotaran.deprecation.modules.test import deprecation_warning_on_call_test_helper
from glotaran.parameter import Parameter


def test_parameter_non_negative():
    """Test that deprecated ``non_negative`` behaves gracefully"""
    notnonneg = Parameter(label="", value=1, non_negative=False)
    valuenotnoneg, _, _ = notnonneg.get_value_and_bounds_for_optimization()
    assert np.allclose(1, valuenotnoneg)
    notnonneg.set_value_from_optimization(valuenotnoneg)
    assert np.allclose(1, notnonneg.value)

    _, nonneg1 = deprecation_warning_on_call_test_helper(
        Parameter, kwargs={"label": "", "value": 1, "non_negative": True}, raise_exception=True
    )
    value1, _, _ = nonneg1.get_value_and_bounds_for_optimization()
    assert np.allclose(1, value1)
    assert nonneg1.non_negative is False
    nonneg1.set_value_from_optimization(value1)
    assert np.allclose(1, nonneg1.value)

    _, nonneg2 = deprecation_warning_on_call_test_helper(
        Parameter,
        kwargs={"label": "", "value": 2, "non_negative": True, "minimum": -1},
        raise_exception=True,
    )
    value2, minimum2, _ = nonneg2.get_value_and_bounds_for_optimization()
    assert np.allclose(2, value2)
    assert nonneg2.non_negative is False
    nonneg2.set_value_from_optimization(value2)
    assert np.allclose(2, nonneg2.value)
    assert np.allclose(0, minimum2)

    _, nonnegminmax = deprecation_warning_on_call_test_helper(
        Parameter,
        kwargs={"label": "", "value": 5, "non_negative": True, "minimum": 3, "maximum": 6},
        raise_exception=True,
    )
    value5, minimum, maximum = nonnegminmax.get_value_and_bounds_for_optimization()
    assert nonnegminmax.non_negative is False
    assert np.allclose(5, value5)
    assert np.allclose(3, minimum)
    assert np.allclose(6, maximum)
