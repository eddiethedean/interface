import typing as _t

class DataMapping(_t.Protocol):
    def __getitem__(self, key: str) -> str:
        ...

    def keys(self) -> _t.Iterable[str]:
        ...

    def values(self) -> _t.Iterable[_t.Sequence]:
        ...

    
    
