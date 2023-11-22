from dataclasses import dataclass
from environs import Env

@dataclass
class EmailConfig:
    host: str
    user: str
    password: str
    port: int
    use_tls: bool

@dataclass
class Server:
    secret_key: str

@dataclass
class DB:
    table: str
    user: str
    password:str

@dataclass
class Config:
    email: EmailConfig
    server: Server
    db: DB

def load_config(path:str=None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(email=EmailConfig(
                                    host=env('EMAIL_HOST'),
                                    user=env('EMAIL_HOST_USER'),
                                    password=env('EMAIL_HOST_PASSWORD'),
                                    port=int(env('EMAIL_PORT')),
                                    use_tls=env('EMAIL_USE_TLS') in ['True', '1']
                                    ),
                  server=Server(
                                secret_key=env('SECRET_KEY')
                                ),
                  db=DB(
                    table=env('DB_TABLE'),
                    user=env('DB_USER'),
                    password=env('DB_PASSWORD')
                  ))
