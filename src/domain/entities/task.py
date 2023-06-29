from dataclasses import dataclass

@dataclass
class Task:
    task_name: str
    task_status: str
    description: str
    id:int = 0


    def to_dict(self):
        return  {
                 "_id" : self.id,
                 "task_name" : self.task_name,
                 "task_status": self.task_status,
                 "description": self.description
                }
    
    def validate_fields(self):
        if not isinstance(self.task_name, str):
            raise TypeError(f"{self.task_name} is not an string")
        if not isinstance(self.task_status, str):
            raise TypeError(f"{self.id} is not an string")
        if len(self.description) > 50:
            raise ValueError(f"{self.description} has too many characters")
    