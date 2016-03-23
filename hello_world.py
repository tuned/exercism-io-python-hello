#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    """
    Return "Hello," plus name or "Hello, World!" 
    """
    return u"Hello, {}!".format(name) if name else "Hello, World!"
