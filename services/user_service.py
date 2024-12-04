from repositories.user_repository import UserRepository
from models.user import User

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def get_all_users(self):
        return await self.repository.read_all()

    async def get_user_by_id(self, user_id):
        return await self.repository.read(user_id)

    async def create_user(self, name, surname, age):
        user = User(await self.repository.get_next_id(), name, surname, age)
        await self.repository.create(user)
        return user

    async def update_user(self, user_id, name, surname, age):
        user = await self.repository.read(user_id)
        if user:
            updated_user = User(user_id, name, surname, age)
            await self.repository.update(user_id, updated_user)
            return updated_user
        return None

    async def delete_user(self, user_id):
        return await self.repository.delete(user_id)
