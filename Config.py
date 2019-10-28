import configparser

cf = configparser.ConfigParser()
cf.read("config.ini")
def getvalue(confname,confvalue):
    return cf.get(confname, confvalue)