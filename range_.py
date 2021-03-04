def range_(start=0, stop=None, step=None):
    """range generator implementation"""
    if (step is None or step > 0) and (stop is None or start < stop):
        step = 1 if step is None else step
        start, stop = (0, start) if stop is None else (start, stop)
        while start < stop:
            yield start
            start += step
    elif (step is None or step < 0) and (stop is not None and start > stop):

        step = -1 if step is None else step
        while start > stop:
            yield start
            start += step


if __name__ == "__main__":
    print(list(range_(10)))
    print(list(range_(10, 14)))
    print(list(range_(10, 14, 0.25)))
    print(list(range_(10, -10)))
    print(list(range_(5, -5, -0.5)))
    print(list(range_(5, -5, 1)))
