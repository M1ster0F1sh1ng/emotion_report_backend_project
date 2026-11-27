from sqlalchemy.ext.asyncio import create_async_engine
URL="mysql+aiomysql://root:020070@localhost:3306/fastapi_test?charset=utf8"
async_engine = create_async_engine(
    URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)