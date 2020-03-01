from threading import Timer
from datetime import date, timedelta, datetime
import yaml
import asyncio

loop = asyncio.get_event_loop()

def swarm(users):
    start_time = datetime.now()
    timers = list()
    scheduled = DELAY

    for step in scenario['steps']:
        timer = Timer(scheduled, swarm, (int(step['users'])))
        timers.append(timer)
        scheduled = scheduled + step['time']

    timers.append(Timer(scheduled, generate_report, (start_time)))

    [t.start() for t in timers]

def stop():
    print('Stopping loop')
    loop.stop()

with open('scenarios.yaml') as file:
    scenarios = yaml.load(file, Loader=yaml.FullLoader)

    exec_delay = 1
    scenario = scenarios['scenarios'][0]

    for step in scenario['steps']:
        print('scheduling {}'.format(step['users']))
        loop.call_later(exec_delay + int(step['time']), swarm, int(step['users']))
        
        # async_call_later(exec_delay, swarm, int(step['users']))
        exec_delay = exec_delay + step['time']
    
    loop.call_later(20, stop)

    try:
        loop.run_forever()
    finally:
        loop.close()


    


# steps:
#     - step:
#     time: 300
#     users: 400

# DELAY = 10 # 10 seconds of delay before to start the swarm

# def swarm(users):
#     print(users)

# def generate_report(start_time):
#     end_time = datetime.now()
#     print('generating reporting of {} to {}', start_time, end_time)

# def run_scenario(scenario):
#     start_time = datetime.now()
#     timers = list()
#     scheduled = DELAY

#     for step in scenario['steps']:
#         timer = Timer(scheduled, swarm, (int(step['users'])))
#         timers.append(timer)
#         scheduled = scheduled + step['time']
    
#     timers.append(Timer(scheduled, generate_report, (start_time)))

#     [t.start() for t in timers]



# with open('scenarios.yaml') as file:
#     scenarios = yaml.load(file, Loader=yaml.FullLoader)
#     for s in scenarios['scenarios']:
#         run_scenario(s)