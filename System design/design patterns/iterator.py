# Iterator is a behavioral design pattern that lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.)
# The main idea of the Iterator pattern is to extract the traversal behavior of a collection into a separate object called an iterator.
# Applicability
#  Use the Iterator pattern when your collection has a complex data structure under the hood, but you want to hide its complexity from clients (either for convenience or security reasons).
#  Use the pattern to reduce duplication of the traversal code across your app.
# Use the Iterator when you want your code to be able to traverse different data structures or when types of these structures are unknown beforehand.

from __future__ import annotations
from collections.abc import Iterable, Iterator

class FacebookIterator(Iterator):
    def __init__(self, FriendsCollection: FacebookCollection, person_name: str) -> None:
        self._collection = FriendsCollection[person_name]
        self._index = 0
        self._person_name = person_name

    def __next__(self) -> str:
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

class FacebookCollection(Iterable):
    def __init__(self) -> None:
        self._friends = {}

    def add_friend(self, person_name: str, friend_name: str) -> None:
        if person_name not in self._friends.keys():
            self._friends[person_name] = []
        self._friends[person_name].append(friend_name)

    def __iter__(self) -> Iterator:
        # Default iteration: iterate over all person names
        return iter(self._friends.keys())

    def iter_for_person(self, person_name: str) -> FacebookIterator:
        return FacebookIterator(self, person_name)

    def __getitem__(self, person_name: str) -> list[str]:
        return self._friends.get(person_name, [])

if __name__ == "__main__":
    friends = FacebookCollection()
    friends.add_friend("Alice", "Bob")
    friends.add_friend("Alice", "Charlie")
    friends.add_friend("Bob", "David")

    # Iterate over all person names
    for person in friends:
        print(f"{person}'s friends: {friends[person]}")

    # Iterate over Alice's friends
    print("Alice's friends:")
    for friend in friends.iter_for_person("Alice"):
        print(friend)