from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    path_id: int
    species: str
    start_location: Habitat
    destination: Habitat
    duration: Optional[int] = None

    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass