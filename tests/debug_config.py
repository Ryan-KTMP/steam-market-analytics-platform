from src.common.app_config import database_config

print("HOST:", repr(database_config.host))
print("PORT:", repr(database_config.port))
print("DB:", repr(database_config.database))
print("USER:", repr(database_config.user))
print("PASSWORD:", repr(database_config.password))