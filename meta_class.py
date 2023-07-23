from typing import List, Tuple, Any

class Day:
    def __run__(self, data: List[str]) -> Any:
        "Method for parsing the data"
        return data

    def part_one(self, data: List[str]) -> Any:
        return 0

    def part_two(self, data: List[str]) -> Any:
        return 0

    @staticmethod
    def __str__() -> str:
        return 'Day'

    def __main__(self, data: List[str] ) -> Tuple[Any, Any]:
        cleaned_data = self.__run__(data)
        return self.part_one(cleaned_data), self.part_two(cleaned_data)