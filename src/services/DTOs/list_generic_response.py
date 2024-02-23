from typing import List, TypeVar

T = TypeVar("T")

class ListGenericResponse:
    def __init__(self, data: List[T], count:int) -> None:
        self.data = data
        self.count = count
