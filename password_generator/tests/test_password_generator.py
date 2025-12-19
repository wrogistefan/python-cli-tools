"""Tests for password generator"""
import pytest
from password_generator.password_generator import PasswordGenerator

def test_default_password_length():
    gen = PasswordGenerator()
    pwd = gen.generate()
    assert len(pwd) == 12

def test_custom_length():
    gen = PasswordGenerator(length=20)
    pwd = gen.generate()
    assert len(pwd) == 20

def test_no_digits():
    gen = PasswordGenerator(use_digits=False)
    pwd = gen.generate()
    assert all(ch not in "0123456789" for ch in pwd)

def test_no_specials():
    gen = PasswordGenerator(use_specials=False)
    pwd = gen.generate()
    specials = "!@#$%^&*()-_=+[]{};:,.<>?/"
    assert all(ch not in specials for ch in pwd)
