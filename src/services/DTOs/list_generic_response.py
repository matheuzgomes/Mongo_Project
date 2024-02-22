from typing import List, TypeVar

K = TypeVar("K")

class ListGenericResponse:
    def __init__(self, data: List[K], count:int) -> None:
        self.data = data
        self.count = count
