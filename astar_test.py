import pytest

from . import astar

def test_basic():
    cases = [
            {
                "label": "Straight line - no obstacles",
                "input": {
                    "maze": [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],
                    "start": (0, 0),
                    "end": (3, 0)
                },
                "expected": [(0, 0), (1, 0), (2, 0), (3, 0),]
            }
            ]

    for case in cases:
        path = astar.astar(case["input"]["maze"], case["input"]["start"], case["input"]["end"])
        print(path)
        assert path == case["expected"]


