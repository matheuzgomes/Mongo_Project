import pytest
from ..src.domain.entities import User


def test_create_user_failed():
    with pytest.raises(TypeError):
        User(
            _id="1",
            username="False",
            password="False",
            name="False",
            description="false",
            is_active=True,
            active_tasks=20,
            task_limit=20,
        ).validate_fields()
