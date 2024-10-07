from typing import Optional, List
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath 
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationManager:
    migrations: dict[int, Migration] = {}
    paths: dict[int, MigrationPath] = {}

    def schedule_migration(self, migration_path: MigrationPath) -> None:
        pass

    def cancel_migration(self, migration_id: int) -> None:
        pass

    def register_migration(self, migration_id: int, start_location: Habitat, destination: Habitat, species: str, duration: Optional[int] = None) -> None:
        pass

    def remove_migration(self, migration_id: int) -> None:
        pass

    def get_migration_by_id(self, migration_id: int) -> Migration:
        pass

    def register_migration_path(self, path_id: int, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def remove_migration_path(self, path_id: int) -> None:
        pass

    def get_migration_path_by_id(self, path_id: int) -> MigrationPath:
        pass