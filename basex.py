"""Encode non-negative integers to strings."""

from typing import Iterator


__all__ = ['encode', 'decode']


def encode(number: int, pool: str) -> str:
    """Encode a non-negative integer as string."""

    if not _has_unique_elements(pool):
        raise ValueError('Pool elements must be unique.')

    if number == 0:
        return pool[0]

    return ''.join(_encode(number, pool))


def decode(code: str, pool: str) -> int:
    """Decode a string into a non-negative integer."""

    if not _has_unique_elements(pool):
        raise ValueError('Pool elements must be unique.')

    return sum(_decode(code, pool))


def _has_unique_elements(pool: str) -> bool:
    """Validates that the pool elements are unique."""

    return len(pool) == len(set(pool))


def _encode(number: int, pool: str) -> Iterator[str]:
    """Encode a non-negative integer as string."""

    base = len(pool)

    while number:
        number, remainder = divmod(number, base)
        yield pool[remainder]


def _decode(code: str, pool: str) -> Iterator[int]:
    """Decode a string into a non-negative integer."""

    base = len(pool)

    for index, char in enumerate(code):
        yield pool.index(char) * (base ** index)
