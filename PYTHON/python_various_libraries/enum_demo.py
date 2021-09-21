from enum import Enum, auto, unique


@unique
class Days(Enum):
    Monday = 1
    # dummy = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = auto()


if __name__ == "__main__":
    print(Days)

    print(Days.Sunday.name)
    print(Days.Sunday.value)

    for day in Days:
        print(f"{day.name} - {day.value}")
