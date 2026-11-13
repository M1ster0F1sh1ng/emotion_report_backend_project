FROM python:3.12-slim
WORKDIR /app
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
COPY pyproject.toml uv.lock ./
RUN uv sync
COPY . .
CMD[ "uvicorn" , "main:app"]