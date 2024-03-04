from dataclasses import dataclass
from typing import Dict, Any
from pydantic import BaseModel

@dataclass
class DeleteDocumentRequest(BaseModel):
    id: int = None
    batch_delete: Dict[str, Any] = None
