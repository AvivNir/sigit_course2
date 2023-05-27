def throw_stop_iteration():
    raise StopIteration("intended exception, don't worry")


def throw_zero_division_error():
    x = 5 / 0


def throw_assertion_error():
    assert False, "AssertionError"


def throw_import_error():
    # import avivs_module
    pass


def throw_key_error():
    my_dict = {"Aviv": "Nir"}
    value = my_dict["notAviv"]


def throw_syntax_error():
    eval("x = 5 +")


def throw_indentation_error():
         print("Aviv")
     # print("Nir")


def throw_type_error():
    x = "five" + 5


if __name__ == '__main__':
    # throw_stop_iteration()
    # throw_zero_division_error()
    # throw_assertion_error()
    # throw_import_error()
    # throw_key_error()
    # throw_syntax_error()
    # throw_indentation_error()
    throw_type_error()