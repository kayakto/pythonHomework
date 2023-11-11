def validate_args(funk):
    def wrapped_funk(*args, **kwargs):
        count = len(args)
        if count < 1:
            return "Not enough arguments"
        elif count > 1:
            return "Too many arguments"
        argument = args[0]
        if not(isinstance(argument, int)):
            return "Wrong types"
        if argument < 0:
            return "Negative argument"
        return funk(*args, **kwargs)
    return wrapped_funk
