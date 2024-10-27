"""
This module contains classes that help handle the file system.
"""

from pathlib import Path

class FileHandler:
    """
    Handler for files.
    """

    @staticmethod
    def find_project_root(start_path: Path = None, marker_file: str = 'rootdir.txt') -> Path:
        """
        Find the outermost directory of the project by searching upwards from start_path
        for the presence of one or more marker files that indicate the project root.
        """
        # If no start path is provided, use the current working directory
        if start_path is None:
            start_path = Path.cwd()

        current_path = start_path.resolve()

        # Traverse upwards through all the paths
        # starting from the current path and its parent
        # a directory containing the marker files (the root) is found
        for parent in [current_path] + list(current_path.parents):
            # If path "${parent}/${marker_file}" exists
            if (parent / marker_file).exists():
                return parent

        # Raise error if no root path found
        raise FileNotFoundError(
            f"Marker file '{marker_file}' not found in any parent directories of '{start_path}'"
        )
