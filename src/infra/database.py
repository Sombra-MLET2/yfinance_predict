from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import infra.configs as configs


engine = create_engine(
    configs.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Method used to get a SQLAlchemy database session.

    FastApi will inject this into a method parameter via:<br/>
        <i>db: Session = Depends(get_db)</i>

    :return: SessionLocal db session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()