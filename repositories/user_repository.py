from models.user import User
import aiofiles
from config import Config

class UserRepository:
    def __init__(self):
        self.file_path = Config.TEXT_DB_PATH

    async def read_all(self):
        async with aiofiles.open(self.file_path, mode='r') as f:
            lines = await f.readlines()
        return [User.from_dict(eval(line.strip())) for line in lines]

    async def read(self, user_id):
        users = await self.read_all()
        for user in users:
            if user.id == user_id:
                return user
        return None

    async def create(self, user):
        async with aiofiles.open(self.file_path, mode='a') as f:
            await f.write(f"{user.to_dict()}\n")

    async def update(self, user_id, updated_user):
        users = await self.read_all()
        async with aiofiles.open(self.file_path, mode='w') as f:
            for user in users:
                if user.id == user_id:
                    await f.write(f"{updated_user.to_dict()}\n")
                else:
                    await f.write(f"{user.to_dict()}\n")

    async def delete(self, user_id):
        users = await self.read_all()
        found = False
        async with aiofiles.open(self.file_path, mode='w') as f:
            for user in users:
                if user.id != user_id:
                    await f.write(f"{user.to_dict()}\n")
                else:
                    found = True
        return found

    async def get_next_id(self):
        users = await self.read_all()
        return max((user.id for user in users), default=0) + 1
