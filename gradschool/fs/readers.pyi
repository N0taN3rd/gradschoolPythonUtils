from csv import DictReader
from typing import Any, Dict, Callable, Generator, List, Optional, Union, TextIO, Iterable
from functools import partial

from ..fn import identity


def stripline(line: str, stripboth: bool = False) -> str: pass


def tail(filep: str, n: int = 10) -> List[str]: pass


def read_plaintext(textfilep: str,
                   mapper: Optional[Callable[[str], Union[str, Any]]] = None) -> Generator[Union[str, Any]]: pass


class CSVFile(object):
    csvin: TextIO
    reader: DictReader

    def __init__(self,
                 csv_path: str,
                 fieldnames: Optional[List[str]] = None,
                 restkey: Optional[str] = None,
                 restval: Optional[str] = None,
                 dialect: str = 'excel',
                 *args: Any, **kwds: Any) -> None: pass

    def __enter__(self) -> DictReader: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass


def read_csv(csv_path: str,
             fieldnames: Optional[List[str]] = None,
             restkey: Optional[str] = None,
             restval: Optional[str] = None,
             dialect: str = 'excel',
             *args: Any, **kwds: Any) -> DictReader: pass


## Try to add some type hinting for json
JsonPrimitive = Union[str, int, float, bool, None]
JsonDict = Dict[str, Union[Dict[str, JsonPrimitive], Dict[str, Any], List[JsonPrimitive], List[Any], Any]]
JsonList = List[Union[JsonPrimitive, List[JsonPrimitive], JsonDict, List[JsonDict], Any]]


class JsonFile(object):
    jsonin: TextIO

    def __init__(self, jsonfp: str) -> None: pass

    def __enter__(self) -> Union[JsonDict, JsonList]: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass


def read_json(jsonfp: str) -> Union[JsonDict, JsonList]: pass


class FilePrinter(object):
    file_obj: TextIO
    line_transformer: Callable[..., Any]

    def __init__(self, file_p: str,
                 line_transformer: Callable[[str], str] = partial(stripline, stripboth=True)) -> None: pass

    def __enter__(self) -> None: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass


class SelectFromFile(object):
    file_obj: TextIO
    line_transformer: Callable[..., Any]
    selector: Callable[..., Any]

    def __init__(self,
                 filep: str,
                 selector: Callable[..., Any] = identity,
                 transformer: Callable[[str], str] = partial(stripline, stripboth=True)) -> None: pass

    def _do_selection(self) -> Generator[Any]: pass

    def __enter__(self) -> Generator[Any]: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass


class CleanFile(object):
    file_p: str
    save_p: str
    file_obj: TextIO
    mapfn: Callable[[str], Any]
    clean_lines: List[Any]
    save_back: bool
    sort_output: Callable[[TextIO], Iterable[str]]

    def __init__(self,
                 filep: str,
                 saveto: Optional[str] = None,
                 save_back: bool = False,
                 mapfn: Callable[..., Any] = identity,
                 sortfn: Callable[..., Any] = identity) -> None: pass

    def __enter__(self) -> List[Any]: pass

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: pass
