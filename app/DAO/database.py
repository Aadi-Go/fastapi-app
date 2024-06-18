from pymongo.errors import OperationFailure
from core import settings
import motor.motor_asyncio


async def db_object():
    client = None
    client: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(settings.DB_URI)
    try:
        client.admin.command('ping')
        print(client.get_default_database(), flush=True)
        print("Connection to DB successful!", flush=True)
        return client
    except Exception as e:
        print("Something went wrong with the DB!", flush=True)
        print(e)
    finally:
        client.close()
        print("Gracefully closing connection with the DB!", flush=True)


async def add_user(username, hashed_password):
    client: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(settings.DB_URI)
    db = client.user_database
    collection = db['user_registrations']
    try:
        result = await collection.insert_one({"username": username, "password": hashed_password})
        return True
    except OperationFailure as e:
        print("Insert failed", flush=True)
        return False


async def get_user(username):
    client: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(settings.DB_URI)
    db = client.user_database
    collection = db['user_registrations']
    user = await collection.find_one({"username": username})
    return user
