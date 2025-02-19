from liiatools.datasets.s903.lds_ssda903_clean import converters


def test_to_category():
    category_dict = [
        {"code": "M1"},
        {"code": "F1"},
        {"code": "MM"},
        {"code": "FF"},
        {"code": "MF"},
    ]
    assert converters.to_category("M1", category_dict) == "M1"
    assert converters.to_category("M2", category_dict) == "error"
    assert converters.to_category("MF", category_dict) == "MF"
    assert converters.to_category("", category_dict) == ""
    assert converters.to_category(None, category_dict) == ""

    category_dict = [{"code": "0", "name": "False"}, {"code": "1", "name": "True"}]
    assert converters.to_category(0, category_dict) == "0"
    assert converters.to_category("false", category_dict) == "0"
    assert converters.to_category(1.0, category_dict) == "1"
    assert converters.to_category("true", category_dict) == "1"
    assert converters.to_category("string", category_dict) == "error"
    assert converters.to_category(123, category_dict) == "error"
    assert converters.to_category("", category_dict) == ""
    assert converters.to_category(None, category_dict) == ""


def test_to_integer():
    assert converters.to_integer("3000", "integer") == 3000
    assert converters.to_integer(123, "integer") == 123
    assert converters.to_integer("date", "") == "date"
    assert converters.to_integer("", "integer") == ""
    assert converters.to_integer(None, "integer") == ""
