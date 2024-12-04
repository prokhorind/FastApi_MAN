from fastapi import APIRouter, HTTPException
from services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/")
async def get_users():
    users = await user_service.get_all_users()
    return [user.to_dict() for user in users]

@router.get("/{user_id}")
async def get_user(user_id: int):
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()

@router.post("/", status_code=201)
async def create_user(name: str, surname: str, age: int):
    user = await user_service.create_user(name, surname, age)
    return user.to_dict()

@router.put("/{user_id}")
async def update_user(user_id: int, name: str, surname: str, age: int):
    user = await user_service.update_user(user_id, name, surname, age)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_dict()

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    if not await user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
