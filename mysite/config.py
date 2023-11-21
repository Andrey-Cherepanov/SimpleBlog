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
class Config:
    email: EmailConfig

def load_config(path:str=None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(email=EmailConfig(
                                    host=env('EMAIL_HOST'),
                                    user=env('EMAIL_HOST_USER'),
                                    password=env('EMAIL_HOST_PASSWORD'),
                                    port=int(env('EMAIL_PORT')),
                                    use_tls=env('EMAIL_USE_TLS') in ['True', '1']
                                    ))
