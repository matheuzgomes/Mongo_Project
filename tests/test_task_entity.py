import pytest
from ..src.domain.entities import Task


def test_create_task_failed():
    with pytest.raises(TypeError):
        Task(
            task_name=2,
            task_status="teste_status",
            description="teste",
            is_active=True,
            user_id=1,
        ).validate_fields()
