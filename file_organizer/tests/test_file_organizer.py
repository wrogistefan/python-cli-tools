"""Tests for file organizer"""

import os
import shutil
import tempfile
import pytest
from ..file_organizer import FileOrganizer


def create_temp_files(base_dir, files):
    """Helper to create dummy files in a temporary directory."""
    for f in files:
        with open(os.path.join(base_dir, f), "w") as fp:
            fp.write("dummy content")


def test_invalid_directory():
    with pytest.raises(ValueError):
        FileOrganizer("not_a_real_dir")


def test_organize_creates_folders_and_moves_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        files = ["doc1.txt", "image1.jpg", "archive1.zip", "noext"]
        create_temp_files(tmpdir, files)

        organizer = FileOrganizer(tmpdir)
        organizer.organize()

        # Check that folders were created
        assert os.path.isdir(os.path.join(tmpdir, "txt"))
        assert os.path.isdir(os.path.join(tmpdir, "jpg"))
        assert os.path.isdir(os.path.join(tmpdir, "zip"))
        assert os.path.isdir(os.path.join(tmpdir, "no_extension"))

        # Check that files were moved
        for f in files:
            ext = os.path.splitext(f)[1].lower().strip(".")
            if not ext:
                ext = "no_extension"
            target_path = os.path.join(tmpdir, ext, f)
            assert os.path.isfile(target_path)


def test_no_files_in_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        organizer = FileOrganizer(tmpdir)
        organizer.organize()
        # Should not create any subfolders
        assert len(os.listdir(tmpdir)) == 0
