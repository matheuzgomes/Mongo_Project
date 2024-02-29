from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class DeleteDocumentRequest:
    id: int = None
    batch_delete: Dict[str, Any] = None
