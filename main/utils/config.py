import os
from dotenv import load_dotenv
from dataclasses import dataclass

# Initialization
load_dotenv(".env.common")
load_dotenv('.env', override=True)

@dataclass
class ServerConfig:
    """
       Server config
    """
    HOST_IP: str
    PORT: str
    NAME: str
    VERSION: str

@dataclass
class PostgreConfig:
    """
       Postgres config
    """
    ENGINE: str
    NAME: str
    HOST_IP: str
    PORT: str
    USER: str
    PASSWORD: str

@dataclass
class Config:
    """
        Config sets
    """
    LOGS_FOLDER_PATH: str
    DJANGO_SETTINGS_MODULE: str
    DEBUG: str
    ALLOWED_HOSTS: str

    POSTGRES:PostgreConfig
    FILE_OPERATION:ServerConfig
    ABSTRACT_METADATA:ServerConfig
    FILE_METADATA:ServerConfig
    MONGO_OPERATION:ServerConfig


config = Config(
    #Default
    LOGS_FOLDER_PATH=os.getenv("LOGS_FOLDER_PATH"),
    DJANGO_SETTINGS_MODULE=os.getenv("DJANGO_SETTINGS_MODULE"),
    DEBUG=os.getenv("DEBUG"),
    ALLOWED_HOSTS=os.getenv("ALLOWED_HOSTS"),

    #POSTGRES
    POSTGRES=PostgreConfig(
        ENGINE=os.getenv("HTTP_POSTGRES_DATABASE_ENGINE"),
        NAME=os.getenv("HTTP_POSTGRES_DATABASE_NAME"),
        HOST_IP=os.getenv("HTTP_POSTGRES_HOST_IP"),
        PORT=os.getenv("HTTP_POSTGRES_PORT"),
        USER=os.getenv("HTTP_POSTGRES_USER"),
        PASSWORD=os.getenv("HTTP_POSTGRES_PASSWORD"),
    ),
    #agent-layer.agent_mgt.file_mgt.file_operation
    FILE_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_OPERATION_PORT"),
        NAME=os.getenv("HTTP_FILE_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_FILE_OPERATION_VERSION"),
    ),
    #agent-layer.agent_mgt.resource_mgt.abstract_metadata
    ABSTRACT_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_ABSTRACT_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_ABSTRACT_METADATA_PORT"),
        NAME=os.getenv("HTTP_ABSTRACT_METADATA_NAME"),
        VERSION=os.getenv("HTTP_ABSTRACT_METADATA_VERSION"),
    ),
    #agent-layer.agent_mgt.resource_mgt.file_metadata
    FILE_METADATA=ServerConfig(
        HOST_IP=os.getenv("HTTP_FILE_METADATA_HOST_IP"),
        PORT=os.getenv("HTTP_FILE_METADATA_PORT"),
        NAME=os.getenv("HTTP_FILE_METADATA_NAME"),
        VERSION=os.getenv("HTTP_FILE_METADATA_VERSION"),
    ),
    #agent-layer.agent_mgt.resource_mgt.mongo_operation
    MONGO_OPERATION=ServerConfig(
        HOST_IP=os.getenv("HTTP_MONGO_OPERATION_HOST_IP"),
        PORT=os.getenv("HTTP_MONGO_OPERATION_PORT"),
        NAME=os.getenv("HTTP_MONGO_OPERATION_NAME"),
        VERSION=os.getenv("HTTP_MONGO_OPERATION_VERSION"),
    )
)
print(config)