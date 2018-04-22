from pathlib import Path
from typing import Callable, Generator, Optional

from gradschool.fn import T


def list_dir(dirpath: str = '.',
             filterfn: Optional[Callable[[Path], bool]] = None) -> Generator[Path]: pass


def list_dirf(dirpath: str = '.',
              filterfn: Callable[[Path], bool] = T) -> Generator[Path]: pass


def rlist_dir(dirpath: str = '.',
              ffilter: Optional[Callable[[Path], bool]] = None,
              dfilter: Optional[Callable[[Path], bool]] = None) -> Generator[Path]: pass


def rlist_dirf(dirpath: str = '.',
               ffilter: Callable[[Path], bool] = T,
               dfilter: Callable[[Path], bool] = T) -> Generator[Path]: pass
