"""
env_specific.py
Generates settings for Django that depend on what environment it's in.
"""
import os

def getAllowedHosts(appEnv):
    if appEnv == "local":
        return ['.localhost', '127.0.0.1', '[::1]']
    elif appEnv == 'azure':
        return [os.environ.get('WEBSITE_HOSTNAME'), os.environ.get('hc_personal_hostname')]
    else:
        return []


def getDBName(appEnv):
    return os.environ.get('AZURE_MYSQL_NAME') if appEnv == 'azure' else os.environ.get('django_db')

def getDBHost(appEnv):
    return os.environ.get('AZURE_MYSQL_HOST') if appEnv == 'azure' else os.environ.get('django_db_host')

def getDBUser(appEnv):
    return os.environ.get('AZURE_MYSQL_USER') if appEnv == 'azure' else os.environ.get('django_db_user')

def getDBPassword(appEnv):
    return os.environ.get('AZURE_MYSQL_PASSWORD') if appEnv == 'azure' else os.environ.get('django_mysql_password', 'NoPasswordEnvVar')

def getDBOptions(appEnv):
    return {'ssl': {'ca': os.environ.get('MYSQL_ATTR_SSL_CA')}} if appEnv == 'azure' else {}