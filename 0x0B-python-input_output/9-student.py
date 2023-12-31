#!/usr/bin/python3
"""Module class Student."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age) -> None:
        """
        Initialize a new Student object

        Args:
            first_name (str): The student first's name.
            last_name (str): The student last's name.
            age (int): The student age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self) -> dict:
        """Retrieves a dictionary representation of the Student."""
        return self.__dict__
