from session_12.models import DB_NAME, DB_HOST, DB_PASS, DB_PORT, DB_USER
from sqlmodel import SQLModel, Session, create_engine


def start_engine(): 
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session