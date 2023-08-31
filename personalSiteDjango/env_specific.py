"""
env_specific.py
Generates settings for Django that depend on what environment it's in.
"""
import os

def getAllowedHosts(appEnv):
    if appEnv == "local":
        from subprocess import Popen, PIPE
        import re
        ips = ['.localhost', '127.0.0.1', '[::1]']
        # get local ip
        allOutput = ""
        with Popen(["ifconfig"], stdout=PIPE) as proc:
            allOutput = str(proc.stdout.read())
        m = re.search(r"wlo1.+inet (?P<localIP>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", allOutput)
        if m and m.group('localIP'):
            ips.append(m.group('localIP'))
            print("local ip: {0}".format(m.group('localIP')))
        return ips
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

def getStorageBase(appEnv):
    return 'TODO' if appEnv == 'azure' else os.environ.get('django_local_storage_base')
