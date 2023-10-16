from sqlalchemy.ext.asyncio import AsyncSession


class DBObjectService:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session
