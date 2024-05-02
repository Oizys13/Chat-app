from pymongo.server_api import  ServerApi
from pymongo.mongo_client import MongoClient
import asyncio
import motor.motor_asyncio




mongo = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B")
db = mongo['bddd']
messages = db['messages']

def printSomething(msg=""):
    print(f"This is printSomething(\"{msg}\")\n\n")







async def  handleWatch():
    async with messages.watch() as stream :
        async for change in stream :
            print('we have a change : ',change['operationType'],'  ',change['fullDocument'])




async def main():
    printSomething("before")
    handleWatch()
    printSomething("after")

asyncio.get_event_loop().run_until_complete(main())

