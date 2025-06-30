"""
This class contains classes to help define new schemas.
"""

class PrereqFormat:
    """
    PrereqFormat is either a course's uid string or a dictionary of courses' uid string lists\n
    with their nested logical operation key ('and', 'or').\n
    """

    def __init__(
            self,
            prereq: dict | str
        ) -> None:
        self._prereq = prereq
        self._check_format()
    
    def _check_format(self):
        """
        Check whether the object is of a correct format.
        """
        
        def dict_traverse(p: str | dict):
            if isinstance(p, str):
                pass
            elif isinstance(p, dict):
                for key in p.keys():
                    if key not in ["and", "or"]:
                        return KeyError(f"Incorrect PrereqFormat's key found: {key}")
                    else:
                        return dict_traverse(p[key])
            else:
                TypeError(
                    f"PrereqFormat can only be a str or dict type." +
                    f"Wrong type found: {type(p)}"
                )
                    
        return dict_traverse(self._prereq)

    def __repr__(self) -> str:
        return (
            f"PrereqFormat(\n"
            f"  prereq = {self._prereq}\n"
            f")"
        )

    def process(self) -> dict | str:
        return self._prereq
