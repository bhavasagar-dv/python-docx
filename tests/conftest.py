"""pytest fixtures that are shared across test modules."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from python_docx import types as t
    from python_docx.parts.story import StoryPart


@pytest.fixture
def fake_parent() -> t.ProvidesStoryPart:
    class ProvidesStoryPart:
        @property
        def part(self) -> StoryPart:
            raise NotImplementedError

    return ProvidesStoryPart()
