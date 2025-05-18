import uuid
from typing import Optional

from support_sphere.models.base import BasePublicSchemaModel
from sqlmodel import Field, Relationship
from datetime import datetime

class ChatRoom(BasePublicSchemaModel, table=True):

    """
    Represents a person to household record mapping in the 'public' schema under 'people_groups' table.

    Attributes
    ----------
    room_id bigint NOT NULL,
    "imageUrl" text,
    metadata jsonb,
    name text,
    room_type text,
    "user_ids" uuid[] NOT NULL,
    "lastMessages" jsonb,
    "user_roles" jsonb,
    "createdAt" bigint NOT NULL,
    "updatedAt" bigint NOT NULL

    Notes
    -----
    """
    __tablename__ = "chat_rooms"

    room_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    image_url: str | None = Field(nullable=True)
    name: str = Field(nullable=False)
    room_type: str = Field(nullable=False)
    user_ids: list["UserProfile"] = Relationship(back_populates="chat_room", cascade_delete=False)
    created_at: datetime = Field(nullable=True)
    updated_at: datetime = Field(nullable=True)