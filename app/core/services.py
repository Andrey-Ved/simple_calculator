from re import compile as re_compile


async def calc(task: str) -> str:
    try:
        # with simple protection
        pattern = re_compile("[a-zA-Z]")

        if pattern.search(task) is None:
            return str(eval(task))

    except (Exception,):
        pass

    return "the task is not correct"
