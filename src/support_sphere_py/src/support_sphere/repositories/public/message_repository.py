from typing import Optional

from sqlmodel import Session, select
from sqlalchemy.orm import joinedload

from support_sphere.models.public import ChatMessage
from support_sphere.repositories.base_repository import BaseRepository


class ChatMessage(BaseRepository):
    """
    Repository class for managing CRUD operations and queries related to the `ChatMessage` model.

    Methods
    -------
    select_all() -> list[ChatMessage]:
        Retrieves all `ChatMessage` records from the database.

    find_by_user(user_id: str) -> list[ChatMessage]:   
        Finds all `ChatMessage` records associated with a specific user.
    
    find_by_room(room_id: str) -> list[ChatMessage]:
        Finds all `ChatMessage` records associated with a specific room.

    find_by_id(id: str) -> Optional[ChatMessage]:
        Finds a `ChatMessage` record by its ID.
    """

    @classmethod
    def select_all(cls) -> list[ChatMessage]:
        """
        Retrieves all `ChatMessage` records from the database.

        Returns
        -------
        list[ChatMessage]
            A list of all `ChatMessage` records.
        """
        return super().select_all(ChatMessage)
    
    @staticmethod
    def find_by_user(user_id: str) -> list[ChatMessage]:
        """
        Finds all `ChatMessage` records associated with a specific user.

        Parameters
        ----------
        user_id : str
            The ID of the user to search for.

        Returns
        -------
        list[ChatMessage]
            A list of `ChatMessage` records associated with the user.
        """
        with Session(ChatMessageRepository.repository_engine) as session:
            statement = select(ChatMessage).where(ChatMessage.author_id == user_id)
            messages = session.exec(statement)
            return messages.all()
    
    @staticmethod
    def find_by_room(room_id: str) -> list[ChatMessage]:
        """
        Finds all `ChatMessage` records associated with a specific room.

        Parameters
        ----------
        room_id : str
            The ID of the room to search for.

        Returns
        -------
        list[ChatMessage]
            A list of `ChatMessage` records associated with the room.
        """
        with Session(ChatMessageRepository.repository_engine) as session:
            statement = select(ChatMessage).where(ChatMessage.room_id == room_id)
            messages = session.exec(statement)
            return messages.all()
    
    @staticmethod
    def find_by_id(id: str) -> Optional[ChatMessage]:
        """
        Finds a `ChatMessage` record by its ID.

        Parameters
        ----------
        id : str
            The ID of the `ChatMessage` record to search for.

        Returns
        -------
        Optional[ChatMessage]
            The `ChatMessage` object if found, otherwise None.
        """
        with Session(ChatMessageRepository.repository_engine) as session:
            statement = select(ChatMessage).where(ChatMessage.id == id)
            message = session.exec(statement).one_or_none()
            return message