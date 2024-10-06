from typing import Any, Optional

class Animal:
    animal_id: int
    species: str
    age: Optional[int] = None
    health_status: Optional[str] = None

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass