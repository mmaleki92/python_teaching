from typing import List

class SortStrategy:
    def sort(self, dataset: List[int]) -> List[int]:
        raise NotImplementedError

class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset):
        return sorted(dataset)  # Simplified for illustration

class QuickSortStrategy(SortStrategy):
    def sort(self, dataset):
        return sorted(dataset)  # Simplified for illustration

class Context:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_data(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)

# Usage
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
context = Context(BubbleSortStrategy())
sorted_data = context.sort_data(data)
print(sorted_data)
