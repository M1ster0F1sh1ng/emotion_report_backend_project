FROM python:3.12-slim
WORKDIR /app
#安装apt,uv
RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
#更新lock
COPY pyproject.toml uv.lock ./
ENV PATH="/root/.local/bin:$PATH"
RUN uv sync
#复制程序
COPY ./app .
EXPOSE 8500
CMD ["uv","run","uvicorn","main:app","--port","8500","--host","0.0.0.0"]
