"""
Unit tests for the BFS algorithm.
"""
import pytest
from bfs import bfs

def test_bfs_disconnected():
    """Test BFS on a disconnected graph."""
    graph = {
        'A': ['B'],
        'B': [],
        'C': ['D'],  # 'C' and 'D' are disconnected from 'A'
        'D': []
    }
    assert set(bfs(graph, 'A')) == {'A', 'B'}  # Fix: Compare as a set

def test_bfs_single_node():
    """Test BFS on a single node graph."""
    graph = {'A': []}
    assert set(bfs(graph, 'A')) == {'A'}  # Fix: Convert to set

def test_bfs_invalid_start():
    """Test BFS with an invalid start node."""
    graph = {'A': ['B'], 'B': []}
    with pytest.raises(ValueError):
        bfs(graph, 'X')  # 'X' is not in the graph

def test_bfs_cycle():
    """Test BFS with a cycle in the graph."""
    graph = {
        'A': ['B'],
        'B': ['A']  # Cycle between A and B
    }
    assert set(bfs(graph, 'A')) == {'A', 'B'}  # Fix: Compare as a set
