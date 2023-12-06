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
class GitHubAuth:
    key: str
    secret_key: str

@dataclass
class GoogleAuth:
    client: str
    secret: str

@dataclass
class SocialAuth:
    github: GitHubAuth
    google: GoogleAuth

@dataclass
class Config:
    email: EmailConfig
    server: Server
    db: DB
    social_auth: SocialAuth


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
                  ),
                  social_auth=SocialAuth(
                    github=GitHubAuth(
                        key=env('SOCIAL_AUTH_GITHUB_KEY'),
                        secret_key=env('SOCIAL_AUTH_GITHUB_SECRET_KEY')
                    ),
                    google=GoogleAuth(
                        client=env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),
                        secret=env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
                    )
                  ))
