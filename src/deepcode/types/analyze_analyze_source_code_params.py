# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AnalyzeAnalyzeSourceCodeParams"]


class AnalyzeAnalyzeSourceCodeParams(TypedDict, total=False):
    code: Required[str]
    """Source code to analyze"""

    language: Required[str]
    """Programming language (e.g., python, javascript)"""
