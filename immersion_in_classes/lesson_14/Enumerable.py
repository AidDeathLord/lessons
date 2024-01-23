from abc import ABC, abstractmethod


class Enumerable(ABC):
    @abstractmethod
    def get_iterator(self):
        raise NotImplementedError("Subclasses must implement this method")

    # BEGIN (write your solution here)

    def max_by(self, fn):
        items = list(self.get_iterator())
        if not items:
            return None
        result = max(items, key=fn)
        return result
