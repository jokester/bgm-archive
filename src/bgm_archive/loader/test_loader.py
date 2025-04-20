#!/usr/bin/env python3
"""
Test script for the ArchiveLoader class.

This script tests the ArchiveLoader with the test_archive.zip file.
"""

import logging
import os
import sys
from pathlib import Path

from bgm_mond.loader.wiki_archive_loader import ArchiveLoader


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def main():
    """Main function."""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Get the path to the test archive
    current_dir = Path(__file__).parent
    test_archive_path = current_dir / "__test_data" / "test_archive.zip"
    
    if not test_archive_path.exists():
        logger.error(f"Test archive not found at {test_archive_path}")
        return
    
    logger.info(f"Loading data from {test_archive_path}")
    loader = ArchiveLoader(str(test_archive_path))
    
    # Test loading each type of data
    test_methods = [
        ("subjects", loader.subjects),
        ("persons", loader.persons),
        ("characters", loader.characters),
        ("episodes", loader.episodes),
        ("subject_relations", loader.subject_relations),
        ("subject_persons", loader.subject_persons),
        ("subject_characters", loader.subject_characters),
        ("person_characters", loader.person_characters),
