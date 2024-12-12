import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from faker import Faker
from pydantic import BaseModel, PastDate

api = FastAPI()
fake = Faker()
chunk_size = 1000
test_data = []

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProfileSchema(BaseModel):
    id: int
    name: str
    birthdate: PastDate
    blood_group: str
    sex: str
    job: str
    company: str


for i in range(chunk_size):
    test_data.append(ProfileSchema(id=i, **fake.profile()))


@api.get("/")
def main():
    return test_data


if __name__ == "__main__":
    uvicorn.run("main:api", port=8080, reload=True)
