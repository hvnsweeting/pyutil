import os
import inspect


def print_and_log_maker(g_log):
    """
    get input logger to use with output function. Create a better
    funtion to log
    """
    log = g_log
    def print_and_log(*args):

        # "Overloading pattern"
        if len(args) == 1:
            debug_level = "i"
            content = args[0]
        else:
            debug_level = args[0]
            content = args[1:]

        if debug_level == "i":
            log.info(content)
        elif debug_level == "c":
            log.critical(content)
        elif debug_level == "d":
            log.debug(content)
        elif debug_level == "w":
            log.warning(content)
        elif debug_level == "e":
            stack = inspect.stack()
            fn_name_cause_error = (stack[1][3],)
            # construct a new tuple
            content = fn_name_cause_error + content
            log.error(content)
        else:
            # many args but no one specify debug level
            # default to INFO
            log.info(content)

        if SIMULATE:
            if debug_level == "e":
                content = "error:" ,content[:50]
            print content
    return print_and_log


def get_abs_path(filename):
    """Return fullpath of file that in same dir with module runs this func"""
    return os.path.join(os.path.dirname(__file__), filename)
