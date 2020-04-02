import filecmp


def my_cmp(a, b):
    return filecmp.cmp(a, b)
