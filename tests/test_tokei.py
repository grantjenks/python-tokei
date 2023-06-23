"""Test Python wrapper for Tokei
"""

import tokei


def test_title():
    assert tokei.__title__ == 'tokei'
