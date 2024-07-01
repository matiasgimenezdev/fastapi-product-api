from models.user import User

users = {
    "johndoe": User(username="johndoe", email="johndoe@example.com", full_name="John Doe",
                    hashed_password="fakehashedsecret"),
    "alice": User(username="alice", email="alice@example.com", full_name="Alice Wonderson",
                  hashed_password="fakehashedsecret2")
}
