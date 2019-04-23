import pytest

from . import astar

def test_basic():
    cases = [{
        "label": "Straight horizontal line - no obstacles",
        "input": {
            "maze": [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],
            "start": (0, 0),
            "end": (3, 0)
            },
        "expected": [(0, 0), (1, 0), (2, 0), (3, 0),]
        },
        {
            "label": "Straight vertical line - no obstacles",
            "input": {
                "maze": [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],
                "start": (0, 0),
                "end": (0, 3)
                },
            "expected": [(0, 0), (0, 1), (0, 2), (0, 3),]
            },
        {
            "label": "Straight horizontal line - obstacles",
            "input": {
                "maze": [[1, 1, 1, 1],[0, 0, 0, 0],[1, 1, 1, 1],[0, 0, 0, 0]],
                "start": (0, 1),
                "end": (3, 1)
                },
            "expected": [(0, 1), (1, 1), (2, 1), (3, 1),]
            },
        {
            "label": "Straight vertical line - obstacles",
            "input": {
                "maze": [[1, 0, 1, 0],[1, 0, 1, 0],[1, 0, 1, 0],[1, 0, 1, 0]],
                "start": (1, 0),
                "end": (1, 3)
                },
            "expected": [(1, 0), (1, 1), (1, 2), (1, 3),]
            },
        {
            "label": "No exit",
            "input": {
                "maze": [[1, 0, 1, 0],[1, 0, 1, 0],[1, 0, 1, 0],[1, 1, 1, 0]],
                "start": (1, 0),
                "end": (1, 3)
                },
            "expected": []
            },
        ]

    for case in cases:
        path = astar.astar(case["input"]["maze"], case["input"]["start"], case["input"]["end"])
        assert path == case["expected"]


def test_advanced():
    cases = [{
        "label": "Vertical wall",
        "input": {
            "maze": [[0, 1, 0, 0],[0, 1, 0, 0],[0, 1, 0, 0],[0, 0, 0, 0]],
            "start": (0, 0),
            "end": (3, 3)
            },
        "expected": [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]
        },
        {
            "label": "Horizontal wall",
            "input": {
                "maze": [[0, 0, 0, 0],[0, 0, 0, 0],[1, 1, 0, 1],[0, 0, 0, 0]],
                "start": (0, 0),
                "end": (3, 3)
                },
            "expected": [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3)]
        },
        {
            "label": "Fake horizontal exit",
            "input": {
                "maze": [[0, 0, 0, 0],[1, 0, 1, 0],[0, 0, 1, 0],[1, 1, 1, 0]],
                "start": (0, 0),
                "end": (3, 3)
                },
            "expected": [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
        },
        {
            "label": "Fake vertical exit",
            "input": {
                "maze": [[0, 1, 0, 0],[0, 0, 1, 0],[0, 1, 0, 0],[0, 0, 0, 0]],
                "start": (1, 0),
                "end": (1, 3)
                },
            "expected": [(1, 0), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3)]
        },
        ]

    for case in cases:
        path = astar.astar(case["input"]["maze"], case["input"]["start"], case["input"]["end"])
        assert path == case["expected"]


