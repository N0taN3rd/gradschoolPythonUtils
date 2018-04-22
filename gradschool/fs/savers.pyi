from contextlib import contextmanager

from typing import TypeVar, SupportsInt, SupportsFloat, \
    MutableMapping, Iterable, Optional, Callable, Tuple, List, \
    Dict, Any, Union

from .formatters import default_formatter

T = TypeVar('T')
A = TypeVar('A')
B = TypeVar('B')
TblCsvV = Union[str, int, float, SupportsInt, SupportsFloat]


def get_accumulator(accu: T) -> T: pass


def selected_data(accu: T, selector: Optional[Callable[..., Iterable]]): pass


@contextmanager
def auto_saver(filepath: str,
               stype: T = list,
               formatter: Callable[..., str] = default_formatter,
               selector: Optional[Callable[..., Iterable]] = None) -> T: pass


@contextmanager
def auto_save2(filep1: str,
               filep2: str,
               accu1: A = list,
               accu2: B = list,
               formater1: Callable[..., str] = default_formatter,
               formater2: Callable[..., str] = default_formatter,
               selector1: Optional[Callable[..., Iterable]] = None,
               selector2: Optional[Callable[..., Iterable]] = None) -> Tuple[A, B]: pass


@contextmanager
def auto_csv(file: str, fieldnames: List[str]) -> List[MutableMapping[TblCsvV, TblCsvV]]: pass


@contextmanager
def auto_latextbl(file: str,
                  headers: Union[str, List[TblCsvV]],
                  accu: T = list) -> T: pass


class AutoSaver(object):
    file: str
    accumulator: T
    formatter: Callable[..., str]
    selector: Optional[Callable[..., Iterable]]

    def __init__(self,
                 file: str,
                 accu: T = list,
                 formatter: Callable[..., str] = default_formatter,
                 selector: Optional[Callable[..., Iterable]] = None) -> None: pass

    def __enter__(self) -> T: pass


class AutoSaveTwo(object):
    f: A
    s: B

    def __init__(self,
                 autos1: Callable[..., A],
                 autos1_args: Dict[str, Any],
                 autos2: Callable[..., B],
                 autos2_args: Dict[str, Any]) -> None: pass

    def __enter__(self) -> Tuple[Any, Any]: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass


class AutoSaveCsv(object):
    accu: List[MutableMapping[TblCsvV, TblCsvV]]
    file: str
    fieldnames: List[str]

    def __init__(self, file: str, fieldnames: List[str]) -> None: pass

    def __enter__(self) -> List[MutableMapping[TblCsvV, TblCsvV]]: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass


class AutoSaveJson(object):
    accu: T
    file: str

    def __init__(self, file: str, accu: T = list) -> None: pass

    def __enter__(self) -> T: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass


class AutoSLatexTable(object):
    accu: T
    file: str
    headers: Union[str, List[TblCsvV]]

    def __init__(self,
                 file: str,
                 headers: Union[str, List[TblCsvV]],
                 accu: T = list) -> None: pass

    def __enter__(self) -> T: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass
