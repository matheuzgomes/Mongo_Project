from dataclasses import dataclass
from datetime import datetime

@dataclass
class Log:
    user_id: int
    log_date: datetime
    function_name: str
    is_success: bool
    error_description: str = None

    def validate_fields(self):
        self.validate_field_type(self.user_id, int, "Invalid User Id")
        self.validate_field_type(self.log_date, datetime, "Invalid Log Date")
        self.validate_field_type(self.function_name, str, "Invalid Function Name")
        self.validate_field_type(self.is_success, bool, "Invalid success option")

    def validate_field_type(self, field, field_type, error_message):
        if not isinstance(field, field_type):
            raise TypeError(error_message)
