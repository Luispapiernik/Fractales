def get_channels(*, mode: str) -> int:
    if mode == "YCbCr":
        return 3

    return len(mode)
