def is_truthy(value):
    return bool(value)


def is_even(n):
    return n % 2 == 0


def has_permission(is_admin, is_logged_in):
    return is_admin and is_logged_in
