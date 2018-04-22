from typing import Any, Callable, DefaultDict, Hashable, Iterable, Iterator, List, NamedTuple, Optional

CacheInfo = NamedTuple(
    'CacheInfo', [
        ('hits', int), ('misses', int), ('maxsize', Optional[int]), ('currentsize', int)])

memowrapper = Callable[..., Any]
memowrapper.cache_info = Callable[[], CacheInfo]
memowrapper.cache_clear = Callable[[], None]
memowrapper.__wrapped__ = Callable[..., Any]


def identity(x: Any) -> Any: pass


def flatmap(iterable: Iterable[Any],
            mapfn: Callable[..., Any]) -> List[Any]: pass


def flatten(iterable: Iterable[Any]) -> List[Any]: pass


def idistinct(iterable: Iterable[Any]) -> Iterator[Any]: pass


def distinct_by(iterable: Iterable[Any],
                keyfn: Callable[...,
                                Hashable]) -> Iterable[Any]: pass


def distinct_by_fn(keyfn: Callable[..., Hashable]
                   ) -> Callable[[Iterable[Any]], Any]: pass


def group_by(iterable: Iterable[Any],
             keyfn: Callable[...,
                             Hashable]) -> DefaultDict[Hashable,
                                                       List[Any]]: pass


def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]: pass


def memoize(fn: Callable[..., Any], cachesize: int = 128,
            typed: bool = False) -> memowrapper: pass


def T(x: Optional[Any] = None) -> True: pass


def F(x: Optional[Any] = None) -> False: pass
