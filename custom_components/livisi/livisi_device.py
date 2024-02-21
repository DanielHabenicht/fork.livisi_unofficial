"""Code to represent a livisi device."""

from __future__ import annotations
from typing import Any

from dataclasses import dataclass

from custom_components.livisi.const import CONTROLLER_DEVICE_TYPES

from .livisi_const import SHC2_ID


@dataclass
class LivisiDevice:
    """Stores the livisi device data."""

    id: str
    type: str
    tags: dict[str, str]
    config: dict[str, Any]
    state: dict[str, Any]
    manufacturer: str
    version: str
    cls: str
    product: str
    desc: str
    capabilities: dict[str, str]
    capability_config: dict[str, dict[str, Any]]
    room: str
    battery_low: bool
    update_available: bool
    updated: bool
    unreachable: bool

    @property
    def name(self) -> str:
        """Get name from config."""
        return self.config.get("name")

    @property
    def tag_category(self) -> str:
        """Get tag type category from config."""
        if self.tags is None:
            return None
        return self.tags.get("typeCategory")

    @property
    def tag_type(self) -> str:
        """Get tag type from config."""
        return self.tags.get("type")

    @property
    def is_shc(self) -> bool:
        """Indicate whether this device is the controller."""
        # TODO: Does this work for V2?
        return self.type in CONTROLLER_DEVICE_TYPES
