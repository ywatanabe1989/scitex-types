"""scitex-types quickstart: type-checking helpers for arrays and lists."""

import scitex_types


def main():
    # 1. is_array_like — recognises numpy arrays, pandas Series, lists, tuples.
    assert scitex_types.is_array_like([1, 2, 3]) is True
    assert scitex_types.is_array_like("not array") is False
    print("is_array_like([1,2,3]):", scitex_types.is_array_like([1, 2, 3]))

    # 2. is_listed_X — predicate over every element of a sequence.
    assert scitex_types.is_listed_X([1, 2, 3], int) is True
    assert scitex_types.is_listed_X([1, "x", 3], int) is False
    print("is_listed_X([1,2,3], int):", scitex_types.is_listed_X([1, 2, 3], int))

    # 3. is_list_of_type — alias style check.
    assert scitex_types.is_list_of_type([1.0, 2.0], float) is True
    print(
        "is_list_of_type([1.0,2.0], float):",
        scitex_types.is_list_of_type([1.0, 2.0], float),
    )

    # 4. ArrayLike / ColorLike protocols are exported as type aliases.
    print("ArrayLike alias:", scitex_types.ArrayLike)
    print("ColorLike alias:", scitex_types.ColorLike)


if __name__ == "__main__":
    main()
