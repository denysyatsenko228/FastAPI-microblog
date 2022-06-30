from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_passeord: str):
    return pwd_context.verify(plain_password, hashed_passeord)


def get_password_hash(password: str):
    return pwd_context.hash(password)
