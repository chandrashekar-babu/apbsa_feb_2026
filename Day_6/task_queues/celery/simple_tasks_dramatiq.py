from time import sleep
import dramatiq

#from dramatiq.brokers.rabbitmq import RabbitmqBroker

#rabbitmq_broker = RabbitmqBroker(host="192.168.1.132")
#dramatiq.set_broker(rabbitmq_broker)

from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="192.168.1.130")
dramatiq.set_broker(redis_broker)

count = 500_000_000

@dramatiq.actor
def add(x, y):
    print("add called...")
    for i in range(count): pass

    return x + y

@dramatiq.actor
def testfn():
    print("testfn invoked...")
    sleep(10)
    return 100
