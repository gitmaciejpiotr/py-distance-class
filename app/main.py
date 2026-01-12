from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, distance: float) -> None:
        self.distance = distance

    def __str__(self) -> str:
        return f"Distance: {self.distance} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.distance})"

    def __add__(self,
                other_distance: Distance | int | float) -> Distance:
        if not isinstance(other_distance, Distance):
            return Distance(
                self.distance + other_distance
            )
        return Distance(
            self.distance + other_distance.distance
        )

    def __iadd__(self,
                 other_distance: Distance | int | float) -> Distance:
        if not isinstance(other_distance, Distance):
            return Distance(
                self.distance + other_distance
            )
        return Distance(
            self.distance + other_distance.distance
        )

    def __mul__(self, other: int | float) -> object:
        return Distance(
            self.distance * other
        )

    def __truediv__(self, other: int | float) -> object:
        return Distance(
            round(self.distance / other, 2)
        )

    def __lt__(self, other: int | float) -> bool:
        return self < other

    def __gt__(self, other: int | float) -> bool:
        return self > other

    def __eq__(self, other: int | float) -> bool:
        return self == other

    def __le__(self, other: int) -> bool:
        return self <= other

    def __ge__(self, other: int) -> bool:
        return self >= other
