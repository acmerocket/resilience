import uuid
from typing import Optional

from support_sphere.models.base import BasePublicSchemaModel
from sqlmodel import Field, Relationship
from geoalchemy2 import Geometry
from datetime import datetime

class ChatMessage(BasePublicSchemaModel, table=True):
    """
    Represents a household record in the 'public' schema under the 'households' table.

    Attributes
    ----------
    id bigint NOT NULL,
    "createdAt" bigint,
    metadata jsonb,
    duration bigint,
    "mimeType" text,
    name text,
    "remoteId" text,
    "repliedMessage" jsonb,
    "roomId" bigint NOT NULL,
    "showStatus" boolean,
    size bigint,
    status text,
    type text,
    "updatedAt" bigint,
    uri text,
    "waveForm" jsonb,
    "isLoading" boolean,
    height double precision,
    width double precision,
    "previewData" jsonb,
    "authorId" uuid NOT NULL,
    text text

    """

    __tablename__ = "messages"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    createdAt: datetime = Field(nullable=False)
    metadata: str | None = Field(nullable=True)
    duration: int | None = Field(nullable=True)
    mimeType: str | None = Field(nullable=True)
    name: str | None = Field(nullable=True)
    remoteId: str | None = Field(nullable=True)
    replied_message: str | None = Field(nullable=True)
    showStatus: bool | None = Field(nullable=True)
    size: int | None = Field(nullable=True)
    status: str | None = Field(nullable=True)
    type: str | None = Field(nullable=True)
    updatedAt: datetime = Field(nullable=True)
    uri: str | None = Field(nullable=True)
    waveForm: str | None = Field(nullable=True)
    isLoading: bool | None = Field(nullable=True)
    height: float | None = Field(nullable=True)
    width: float | None = Field(nullable=True)
    preview_data: str | None = Field(nullable=True)
    author_id: uuid.UUID = Field(foreign_key="auth.users.id")
    text: str | None = Field(nullable=True)

    rooom: Optional["ChatRoom"] = Relationship(back_populates="chat_room", cascade_delete=False)

