#!/usr/bin/env python3
"""Tests for contrast.py. Run: python3 scripts/test_contrast.py"""
import contrast as c


def approx(a, b, tol=0.05):
    return abs(a - b) <= tol


def run():
    # Known reference ratios.
    assert approx(c.contrast_ratio((0, 0, 0), (255, 255, 255)), 21.0), "black/white should be 21:1"
    assert approx(c.contrast_ratio((255, 255, 255), (255, 255, 255)), 1.0), "same color should be 1:1"
    # WebAIM reference: #E57373 on #FFFFFF ~ 2.89:1
    assert approx(c.contrast_ratio(c.parse_color("#E57373"), c.parse_color("#FFFFFF")), 2.89, 0.1)
    # #C62828 on white ~ 5.9:1
    assert approx(c.contrast_ratio(c.parse_color("#C62828"), c.parse_color("#FFFFFF")), 5.62, 0.1)
    # Parsing variants.
    assert c.parse_color("#fff") == (255, 255, 255)
    assert c.parse_color("#000000") == (0, 0, 0)
    assert c.parse_color("rgb(230,115,115)") == (230, 115, 115)
    assert c.parse_color("rgba(0, 0, 0, 0.5)") == (0, 0, 0)
    assert c.parse_color("white") == (255, 255, 255)
    # Large-text rule.
    assert c.is_large(24) is True
    assert c.is_large(20) is False
    assert c.is_large(19, bold=True) is True
    # Assessment thresholds.
    a = c.assess(4.5)  # normal text
    assert a["text_AA"] and not a["text_AAA"]
    a2 = c.assess(3.2, size_px=30)  # large text
    assert a2["text_AA"] and a2["ui_component_AA"] and not a2["text_AAA"]
    a3 = c.assess(2.9)
    assert not a3["text_AA"] and not a3["ui_component_AA"]
    # Errors.
    for bad in ["notacolor", "#12", "rgb(300,0,0)", "transparent"]:
        try:
            c.parse_color(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError for " + bad)
    print("all tests passed")


if __name__ == "__main__":
    run()
