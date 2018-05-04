import pymongo
import redis


class MongoDB:
    @staticmethod
    def client():
        return pymongo.MongoClient('mongodb', 27017).test


class RedisDB:
    @staticmethod
    def client():
        return redis.Redis(host='redis-server', port=6379, decode_responses=True)
