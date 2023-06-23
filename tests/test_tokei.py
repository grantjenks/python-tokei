"""Test Python wrapper for Tokei"""
import pytest
import tokei


def test_title():
    assert tokei.__title__ == 'tokei'


def test_tokei():
    result = tokei.tokei(__file__)
    assert result['Total']['code'] > 0


def test_tokei_bad_path():
    with pytest.raises(Exception):
        tokei.tokei('does-not-exist')
