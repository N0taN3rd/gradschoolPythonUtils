from typing import Callable, Any


def default_formatter(item: Any) -> str: pass


def int_formatter(i: int) -> str: pass


def formatter_str(formatstr: str) -> Callable[..., str]: pass


def custom_formatter(selector: Callable[..., str], formatstr: str) -> Callable[..., str]: pass


def format_output(tosave: Any, formatter: Callable[..., str]) -> str: pass
