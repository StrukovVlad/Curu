""" Вносим изменения в doxstream"""

header = "Say hello in Python"

def hello(name: str) -> str:
    """
    %s

    Python is amazing!
    """
    return f"Hello {name}. Nice to meet you!!!"

hello.__doc__%=header
help(hello)

# Help on function hello in module __main__:

# hello(name: str) -> str
   # Say hello in Python

   # Python is amazing!

header = "Produce the result we need"

def hello(arg1, arg2):
    """
    %s

    It is reality good, you should use

    """
    return arg1+arg2

hello.__doc__%=header
help(hello)

# Help on function hello in module __main__:

# hello(arg1, arg2)
    # Produce the result we need

    # It is reality good, you should use
