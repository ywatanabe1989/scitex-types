#!/usr/bin/env python3
# File: ./tests/scitex/types/test__is_listed_X.py
# ----------------------------------------

"""Tests for scitex_types._is_listed_X module."""

import pytest

# numpy is an optional extra (scitex-types[numpy]), so guard at module-import
# time (PA-303). Skips the whole file if numpy isn't installed.
np = pytest.importorskip("numpy")

from scitex_types._is_listed_X import is_list_of_type, is_listed_X

# ===========================================================================
# is_listed_X — basic callability / API surface
# ===========================================================================


def test_is_listed_X_function_is_callable():
    # Arrange
    # Act
    callable_flag = callable(is_listed_X)
    # Assert
    assert callable_flag


# ===========================================================================
# Simple same-type lists pass
# ===========================================================================


def test_list_of_integers_against_int_returns_true():
    # Arrange
    obj = [1, 2, 3, 4, 5]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert result is True or result == True  # noqa: E712


def test_list_of_strings_against_str_returns_true():
    # Arrange
    obj = ["a", "b", "c"]
    # Act
    result = is_listed_X(obj, str)
    # Assert
    assert bool(result) is True


def test_list_of_floats_against_float_returns_true():
    # Arrange
    obj = [1.0, 2.5, 3.14]
    # Act
    result = is_listed_X(obj, float)
    # Assert
    assert bool(result) is True


# ===========================================================================
# Mixed-type lists fail single-type checks
# ===========================================================================


@pytest.mark.parametrize("typ", [int, str, float])
def test_mixed_list_fails_each_single_type(typ):
    # Arrange
    obj = [1, "a", 3.0]
    # Act
    result = is_listed_X(obj, typ)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Tuple/list "allowed types" arg
# ===========================================================================


def test_all_int_passes_int_or_float_tuple():
    # Arrange
    obj = [1, 2, 3]
    # Act
    result = is_listed_X(obj, (int, float))
    # Assert
    assert bool(result) is True


def test_all_float_passes_int_or_float_tuple():
    # Arrange
    obj = [1.0, 2.5, 3.14]
    # Act
    result = is_listed_X(obj, (int, float))
    # Assert
    assert bool(result) is True


def test_mixed_int_float_fails_int_or_float_tuple():
    # Arrange
    obj = [1, 2.5, 3]
    # Act
    result = is_listed_X(obj, (int, float))
    # Assert
    assert bool(result) is False


def test_all_int_passes_int_or_float_list():
    # Arrange
    obj = [1, 2, 3]
    # Act
    result = is_listed_X(obj, [int, float])
    # Assert
    assert bool(result) is True


def test_all_float_passes_int_or_float_list():
    # Arrange
    obj = [1.0, 2.5, 3.14]
    # Act
    result = is_listed_X(obj, [int, float])
    # Assert
    assert bool(result) is True


def test_mixed_int_float_fails_int_or_float_list():
    # Arrange
    obj = [1, 2.5, 3]
    # Act
    result = is_listed_X(obj, [int, float])
    # Assert
    assert bool(result) is False


# ===========================================================================
# Empty list — vacuously true for any type
# ===========================================================================


def test_empty_list_passes_int():
    # Arrange
    obj = []
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is True


def test_empty_list_passes_str():
    # Arrange
    obj = []
    # Act
    result = is_listed_X(obj, str)
    # Assert
    assert bool(result) is True


def test_empty_list_passes_int_or_float_tuple():
    # Arrange
    obj = []
    # Act
    result = is_listed_X(obj, (int, float))
    # Assert
    assert bool(result) is True


# ===========================================================================
# Non-list inputs always fail
# ===========================================================================


@pytest.mark.parametrize(
    "obj",
    [
        "not a list",
        123,
        {"a": 1},
        (1, 2, 3),
        np.array([1, 2, 3]),
    ],
)
def test_non_list_object_returns_false(obj):
    # Arrange
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Nested lists
# ===========================================================================


def test_list_of_lists_against_list_type_returns_true():
    # Arrange
    obj = [[1, 2], [3, 4]]
    # Act
    result = is_listed_X(obj, list)
    # Assert
    assert bool(result) is True


def test_list_of_lists_against_int_type_returns_false():
    # Arrange
    obj = [[1, 2], [3, 4]]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is False


# ===========================================================================
# None values
# ===========================================================================


def test_list_with_none_against_int_returns_false():
    # Arrange
    obj = [1, None, 3]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is False


def test_mixed_int_and_none_fails_int_or_none_tuple():
    # Arrange
    obj = [1, None, 3]
    # Act
    result = is_listed_X(obj, (int, type(None)))
    # Assert
    assert bool(result) is False


def test_all_none_passes_int_or_none_tuple():
    # Arrange
    obj = [None, None, None]
    # Act
    result = is_listed_X(obj, (int, type(None)))
    # Assert
    assert bool(result) is True


def test_all_none_passes_none_type():
    # Arrange
    obj = [None, None, None]
    # Act
    result = is_listed_X(obj, type(None))
    # Assert
    assert bool(result) is True


# ===========================================================================
# Complex / bool / numpy types
# ===========================================================================


def test_list_of_complex_passes_complex_type():
    # Arrange
    obj = [complex(1, 2), complex(3, 4)]
    # Act
    result = is_listed_X(obj, complex)
    # Assert
    assert bool(result) is True


def test_list_of_complex_fails_int_type():
    # Arrange
    obj = [complex(1, 2), complex(3, 4)]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is False


def test_list_of_bool_passes_bool_type():
    # Arrange
    obj = [True, False, True]
    # Act
    result = is_listed_X(obj, bool)
    # Assert
    assert bool(result) is True


def test_list_of_bool_passes_int_type_via_inheritance():
    # Arrange
    obj = [True, False, True]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is True


def test_list_of_np_int32_passes_np_int32_type():
    # Arrange
    obj = [np.int32(1), np.int32(2), np.int32(3)]
    # Act
    result = is_listed_X(obj, np.int32)
    # Assert
    assert bool(result) is True


def test_list_of_np_int32_fails_python_int_type():
    # Arrange
    obj = [np.int32(1), np.int32(2), np.int32(3)]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Custom class instances
# ===========================================================================


class _CustomClass:
    def __init__(self, value):
        self.value = value


def test_list_of_custom_instances_passes_custom_class():
    # Arrange
    obj = [_CustomClass(1), _CustomClass(2)]
    # Act
    result = is_listed_X(obj, _CustomClass)
    # Assert
    assert bool(result) is True


def test_list_of_custom_instances_fails_int_type():
    # Arrange
    obj = [_CustomClass(1), _CustomClass(2)]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Exception handling
# ===========================================================================


def test_none_input_returns_false():
    # Arrange
    # Act
    result = is_listed_X(None, int)
    # Assert
    assert bool(result) is False


def test_problematic_class_does_not_raise():
    # Arrange
    class ProblematicClass:
        def __hash__(self):
            raise TypeError("Unhashable type")

    obj = [ProblematicClass()]
    # Act
    result = is_listed_X(obj, ProblematicClass)
    # Assert
    assert isinstance(result, (bool, np.bool_))


# ===========================================================================
# Large list performance
# ===========================================================================


def test_large_int_list_passes_int_type():
    # Arrange
    obj = list(range(1000))
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is True


def test_large_int_list_fails_str_type():
    # Arrange
    obj = list(range(1000))
    # Act
    result = is_listed_X(obj, str)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Strings vs bytes
# ===========================================================================


def test_list_of_strings_fails_bytes_type():
    # Arrange
    obj = ["hello", "world", "test"]
    # Act
    result = is_listed_X(obj, bytes)
    # Assert
    assert bool(result) is False


def test_list_of_bytes_passes_bytes_type():
    # Arrange
    obj = [b"hello", b"world"]
    # Act
    result = is_listed_X(obj, bytes)
    # Assert
    assert bool(result) is True


def test_list_of_bytes_fails_str_type():
    # Arrange
    obj = [b"hello", b"world"]
    # Act
    result = is_listed_X(obj, str)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Function objects
# ===========================================================================


def test_list_of_functions_passes_function_type():
    # Arrange
    def func1():
        pass

    def func2():
        pass

    obj = [func1, func2]
    # Act
    result = is_listed_X(obj, type(func1))
    # Assert
    assert bool(result) is True


# ===========================================================================
# Single-element edge cases
# ===========================================================================


def test_single_int_list_passes_int():
    # Arrange
    # Act
    result = is_listed_X([1], int)
    # Assert
    assert bool(result) is True


def test_single_int_list_fails_str():
    # Arrange
    # Act
    result = is_listed_X([1], str)
    # Assert
    assert bool(result) is False


def test_single_string_list_passes_str():
    # Arrange
    # Act
    result = is_listed_X(["a"], str)
    # Assert
    assert bool(result) is True


def test_single_string_list_fails_int():
    # Arrange
    # Act
    result = is_listed_X(["a"], int)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Return type is always boolean-ish
# ===========================================================================


@pytest.mark.parametrize(
    "obj, types",
    [
        ([1, 2, 3], int),
        (["a", "b"], str),
        ([1, "a"], int),
        (None, int),
        ("not_a_list", str),
        ([], int),
    ],
)
def test_return_type_is_boolean_for_each_input(obj, types):
    # Arrange
    # Act
    result = is_listed_X(obj, types)
    # Assert
    assert isinstance(result, (bool, np.bool_))


# ===========================================================================
# Docstring examples
# ===========================================================================


def test_docstring_example_passes_int():
    # Arrange
    obj = [3, 2, 1, 5]
    # Act
    result = is_listed_X(obj, int)
    # Assert
    assert bool(result) is True


def test_docstring_example_passes_int_or_float():
    # Arrange
    obj = [3, 2, 1, 5]
    # Act
    result = is_listed_X(obj, (int, float))
    # Assert
    assert bool(result) is True


def test_docstring_example_fails_str():
    # Arrange
    obj = [3, 2, 1, 5]
    # Act
    result = is_listed_X(obj, str)
    # Assert
    assert bool(result) is False


# ===========================================================================
# is_list_of_type alias
# ===========================================================================


def test_is_list_of_type_alias_is_callable():
    # Arrange
    # Act
    callable_flag = callable(is_list_of_type)
    # Assert
    assert callable_flag


def test_alias_int_list_matches_original():
    # Arrange
    obj = [1, 2, 3, 4, 5]
    # Act
    matches = is_list_of_type(obj, int) == is_listed_X(obj, int)
    # Assert
    assert matches


def test_alias_int_list_str_check_matches_original():
    # Arrange
    obj = [1, 2, 3, 4, 5]
    # Act
    matches = is_list_of_type(obj, str) == is_listed_X(obj, str)
    # Assert
    assert matches


def test_alias_str_list_str_check_matches_original():
    # Arrange
    obj = ["a", "b", "c"]
    # Act
    matches = is_list_of_type(obj, str) == is_listed_X(obj, str)
    # Assert
    assert matches


def test_alias_str_list_int_check_matches_original():
    # Arrange
    obj = ["a", "b", "c"]
    # Act
    matches = is_list_of_type(obj, int) == is_listed_X(obj, int)
    # Assert
    assert matches


def test_alias_empty_list_int_matches_original():
    # Arrange
    # Act
    matches = is_list_of_type([], int) == is_listed_X([], int)
    # Assert
    assert matches


def test_alias_empty_list_str_matches_original():
    # Arrange
    # Act
    matches = is_list_of_type([], str) == is_listed_X([], str)
    # Assert
    assert matches


def test_alias_non_list_string_input_matches_original():
    # Arrange
    # Act
    matches = is_list_of_type("not a list", int) == is_listed_X("not a list", int)
    # Assert
    assert matches


def test_alias_non_list_int_input_matches_original():
    # Arrange
    # Act
    matches = is_list_of_type(123, int) == is_listed_X(123, int)
    # Assert
    assert matches


def test_alias_none_input_matches_original():
    # Arrange
    # Act
    matches = is_list_of_type(None, int) == is_listed_X(None, int)
    # Assert
    assert matches


def test_alias_int_float_tuple_matches_original():
    # Arrange
    obj = [1, 2, 3]
    # Act
    matches = is_list_of_type(obj, (int, float)) == is_listed_X(obj, (int, float))
    # Assert
    assert matches


def test_alias_int_str_list_matches_original():
    # Arrange
    obj = [1, 2, 3]
    # Act
    matches = is_list_of_type(obj, [int, str]) == is_listed_X(obj, [int, str])
    # Assert
    assert matches


def test_alias_int_list_basic_returns_true():
    # Arrange
    # Act
    result = is_list_of_type([1, 2, 3], int)
    # Assert
    assert bool(result) is True


def test_alias_string_list_basic_returns_true():
    # Arrange
    # Act
    result = is_list_of_type(["a", "b"], str)
    # Assert
    assert bool(result) is True


def test_alias_float_list_basic_returns_true():
    # Arrange
    # Act
    result = is_list_of_type([1.0, 2.0], float)
    # Assert
    assert bool(result) is True


def test_alias_mixed_list_fails_single_type():
    # Arrange
    # Act
    result = is_list_of_type([1, "a"], int)
    # Assert
    assert bool(result) is False


# ===========================================================================
# Module-level integration
# ===========================================================================


def test_scitex_types_module_exposes_is_listed_X():
    # Arrange
    import scitex_types

    # Act
    has_attr = hasattr(scitex_types, "is_listed_X")
    # Assert
    assert has_attr


def test_scitex_types_module_exposes_is_list_of_type():
    # Arrange
    import scitex_types

    # Act
    has_attr = hasattr(scitex_types, "is_list_of_type")
    # Assert
    assert has_attr


def test_module_is_listed_X_is_same_object():
    # Arrange
    import scitex_types

    # Act
    same = scitex_types.is_listed_X is is_listed_X
    # Assert
    assert same


def test_module_is_list_of_type_is_same_object():
    # Arrange
    import scitex_types

    # Act
    same = scitex_types.is_list_of_type is is_list_of_type
    # Assert
    assert same


def test_is_listed_X_listed_in_module_all():
    # Arrange
    import scitex_types

    # Act
    is_in_all = "is_listed_X" in scitex_types.__all__
    # Assert
    assert is_in_all


def test_is_list_of_type_listed_in_module_all():
    # Arrange
    import scitex_types

    # Act
    is_in_all = "is_list_of_type" in scitex_types.__all__
    # Assert
    assert is_in_all
