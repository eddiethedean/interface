import typing as _t

@_t.runtime_checkable
class DataMapping(_t.Protocol):
    def __getitem__(self, key: str) -> str:
        ...

    def keys(self) -> _t.Iterable[str]:
        ...

    def values(self) -> _t.Iterable[_t.Sequence]:
        ...

    
    
