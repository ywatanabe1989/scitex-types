#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: ./tests/scitex/types/test__ColorLike.py

"""Tests for ColorLike type definition."""

import inspect
from typing import get_args, get_origin

import pytest

from scitex_types import ColorLike

# ---------------------------------------------------------------------------
# Union structure
# ---------------------------------------------------------------------------


def test_colorlike_union_has_args():
    # Arrange
    # Act
    args = get_args(ColorLike)
    # Assert
    assert args is not None


def test_colorlike_union_has_at_least_three_members():
    # Arrange
    # Act
    args = get_args(ColorLike)
    # Assert
    assert len(args) >= 3


def test_colorlike_union_includes_string_type():
    # Arrange
    # Act
    args = get_args(ColorLike)
    # Assert
    assert str in args


def test_colorlike_union_includes_tuple_type():
    # Arrange
    args = get_args(ColorLike)
    # Act
    tuple_args = [a for a in args if get_origin(a) is tuple or a is tuple]
    # Assert
    assert len(tuple_args) > 0


def test_colorlike_union_includes_list_type():
    # Arrange
    args = get_args(ColorLike)
    # Act
    list_types = [a for a in args if get_origin(a) is list or a is list]
    # Assert
    assert len(list_types) > 0


# ---------------------------------------------------------------------------
# Use in annotations
# ---------------------------------------------------------------------------


def test_colorlike_usable_as_parameter_annotation():
    # Arrange
    def fn(color: ColorLike) -> str:
        return str(color)

    # Act
    annotation = fn.__annotations__["color"]
    # Assert
    assert annotation is ColorLike


def test_colorlike_parameter_annotation_introspectable():
    # Arrange
    def plot_with_color(data, color: ColorLike):
        return f"Plotting with color: {color}"

    # Act
    sig = inspect.signature(plot_with_color)
    # Assert
    assert sig.parameters["color"].annotation is ColorLike


def test_colorlike_return_annotation_introspectable():
    # Arrange
    def get_default_color() -> ColorLike:
        return "blue"

    # Act
    sig = inspect.signature(get_default_color)
    # Assert
    assert sig.return_annotation is ColorLike


def test_colorlike_variable_annotation_for_string():
    # Arrange
    primary_color: ColorLike = "red"
    # Act
    # Assert
    assert primary_color == "red"


def test_colorlike_variable_annotation_for_tuple():
    # Arrange
    secondary_color: ColorLike = (0.0, 1.0, 0.0)
    # Act
    # Assert
    assert secondary_color == (0.0, 1.0, 0.0)


def test_colorlike_variable_annotation_for_list():
    # Arrange
    tertiary_color: ColorLike = [0.0, 0.0, 1.0]
    # Act
    # Assert
    assert tertiary_color == [0.0, 0.0, 1.0]


# ---------------------------------------------------------------------------
# String / tuple / list members in detail
# ---------------------------------------------------------------------------


def test_colorlike_includes_str_for_named_colors():
    # Arrange
    args = get_args(ColorLike)
    # Act
    type_names = [str(a) for a in args]
    # Assert
    assert any("str" in name for name in type_names)


def test_colorlike_includes_tuple_for_rgb():
    # Arrange
    args = get_args(ColorLike)
    # Act
    type_names = [str(a).lower() for a in args]
    # Assert
    assert any("tuple" in name for name in type_names)


def test_colorlike_includes_list_for_color_arrays():
    # Arrange
    args = get_args(ColorLike)
    # Act
    type_names = [str(a).lower() for a in args]
    # Assert
    assert any("list" in name for name in type_names)


# ---------------------------------------------------------------------------
# Module integration
# ---------------------------------------------------------------------------


def test_colorlike_exposed_on_scitex_types_module():
    # Arrange
    import scitex_types

    # Act
    has_attr = hasattr(scitex_types, "ColorLike")
    # Assert
    assert has_attr


def test_colorlike_module_attribute_is_same_object():
    # Arrange
    import scitex_types

    # Act
    same = scitex_types.ColorLike is ColorLike
    # Assert
    assert same


# ---------------------------------------------------------------------------
# Realistic usage scenarios (each split to one assertion)
# ---------------------------------------------------------------------------


@pytest.fixture
def plot_color_result():
    def set_plot_colors(
        line_color: ColorLike,
        fill_color: ColorLike,
        background_color: ColorLike,
    ):
        return {
            "line": line_color,
            "fill": fill_color,
            "background": background_color,
        }

    return set_plot_colors("red", (0.0, 1.0, 0.0), [0.0, 0.0, 1.0])


def test_plot_color_dict_preserves_line_string(plot_color_result):
    # Arrange
    # Act
    line = plot_color_result["line"]
    # Assert
    assert line == "red"


def test_plot_color_dict_preserves_fill_tuple(plot_color_result):
    # Arrange
    # Act
    fill = plot_color_result["fill"]
    # Assert
    assert fill == (0.0, 1.0, 0.0)


def test_plot_color_dict_preserves_background_list(plot_color_result):
    # Arrange
    # Act
    background = plot_color_result["background"]
    # Assert
    assert background == [0.0, 0.0, 1.0]
