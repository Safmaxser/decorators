import logging
from functools import wraps


def logger(old_function):
    logging.basicConfig(level=logging.INFO, filename="main.log",
                        filemode="w", encoding="utf-8", force=True,
                        format="%(asctime)s %(levelname)s %(message)s")

    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        logging.info(f'Функция: {old_function.__name__} '
                     f'с аргументами {args} {kwargs} '
                     f'возвращен результат {result}')
        return result
    return new_function


def logger_path(path):
    logging.basicConfig(level=logging.INFO, filename=path,
                        filemode="w", encoding="utf-8", force=True,
                        format="%(asctime)s %(levelname)s %(message)s")

    def __logger(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            logging.info(f'Функция: {old_function.__name__} '
                         f'с аргументами {args} {kwargs} '
                         f'возвращен результат {result}')
            return result
        return new_function
    return __logger
