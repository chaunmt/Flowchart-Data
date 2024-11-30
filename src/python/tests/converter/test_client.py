"""
This module contains tests for client's converters.
"""

# pylint: disable=protected-access,invalid-name

import pytest
from ...converter.client import FlowchartConverter

class TestFlowchartConverter:
    """
    This class contains tests for the FlowchartConverter class.
    """

    #############################################################################
    @pytest.mark.parametrize("original, expected", [
        # Expect changes
        ({"and": ["003675"]}, "003675"),
        ({"or": ["003675"]}, "003675"),
        (["003675"], "003675"),
        # Expect no changes
        ({}, {}),
        ("003675", "003675"),
        (["809667","810346"], ["809667","810346"]),
        ({"and": ["809667","810346"]}, {"and": ["809667","810346"]}),
        ({"or": ["809667","810346"]}, {"or": ["809667","810346"]}),
        (
            {"and": [
                {"or": ["003675", "123675"]},
                {"and": ["809667", "810346"]},
                "802446"
            ]},
            {"and": [
                {"or": ["003675", "123675"]},
                {"and": ["809667", "810346"]},
                "802446"
            ]}
        )
    ])
    def test_break_one_child_nest(self, original, expected):
        """
        Test the break_one_child_nest method.
        """

        converter = FlowchartConverter(original)
        result = converter.break_one_child_nest(converter._prereq)

        assert result == expected, f"From: {original}, Expected: {expected}, Got: {result}"
