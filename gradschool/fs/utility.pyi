from pathlib import Path
import os

def as_pathlib(path: str) -> Path: pass

def as_uri(path: str) -> str: pass

def isfile(path: str) -> bool: pass

def isdir(path: str) -> bool: pass

def is_absolute(path: str) -> bool: pass

def join_with_cwd(name: str) -> str: pass

def basename(name: str) -> str: pass

def dirname(name: str) -> str: pass

def rename(pfrom: str, pto: str) -> None: pass

def samefile(path1: str, path2: str) -> bool: pass

def path_exists(path: str) -> bool: pass

def relpath(path: str, start: str = os.curdir) -> str: pass

def resolve(path: str) -> str: pass


