import pytest
import asyncio
from contextlib import nullcontext as does_not_raise
from datetime import datetime
from ..src.domain.entities import Task
from ..src.infra.repositories import TaskRepository
from ..src.infra.db_handler import DbHandler

test_task = Task(
            task_name=2,
            task_status="teste_status",
            description="teste",
            is_active=True,
            user_id=1,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            tags=[1, 2])

test_task_2 = Task(
            task_name=3,
            task_status="teste_status",
            description="teste",
            is_active=True,
            user_id=1,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            tags=[1, 2])

test_task_3 = Task(
            task_name="Successfull task creation",
            task_status="teste_status",
            description="teste",
            is_active=True,
            user_id=1,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            tags=[1, 2])

@pytest.mark.parametrize(
        "task, expectation, message",[
            (test_task, pytest.raises(TypeError), "2 is not a string"),
            (test_task_2, pytest.raises(TypeError), "3 is not a string"),
            (test_task_3, does_not_raise(), None),

        ],
)
def test_create_task(task: Task, expectation, message):
    with expectation as e:
        task.validate_fields()
    assert message is None or message in str(e)

@pytest.mark.parametrize(
        "user_id", [
            (7)
        ]
)
@pytest.mark.asyncio
async def test_get_all_tasks_repository(user_id:int, repo = TaskRepository):
    _, get_tasks = await repo(DbHandler()).find_all_by_user_id(user_id=user_id)
    assert [item['user_id'] == user_id for item in get_tasks]


@pytest.mark.parametrize(
        "user_id, task_id", [
            (7, 5)
        ]
)
@pytest.mark.asyncio
async def test_get_task_by_id_repository(user_id:int, task_id: int, repo = TaskRepository):
    get_task = await repo(DbHandler()).find_one_by_id(user_id=user_id, task_id=task_id)
    assert task_id == get_task["_id"] and user_id == get_task["user_id"]



@pytest.mark.parametrize(
        "search_field, value_searched, user_id", [
            ("task_name", "testing", 7)
        ]
)
@pytest.mark.asyncio
async def test_get_task_by_generic_str_field(
    search_field: str,
    value_searched: str,
    user_id: int,
    repo = TaskRepository
    ):

    get_task = await repo(DbHandler()).find_one_by_generic_string_field(
        search_field=search_field,
        user_id=user_id,
        value_searched=value_searched
        )

    assert get_task["user_id"] == user_id and get_task["task_name"] == value_searched
