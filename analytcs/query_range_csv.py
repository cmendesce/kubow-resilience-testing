"""
A simple program to print the result of a Prometheus query as CSV.
"""

import requests
import sys
import pandas as pd 
import numpy as np
from datetime import date, timedelta, datetime
import yaml
import matplotlib.pyplot as plt

def query_range(host, start, end, query, columns):
    response = requests.get('{0}/api/v1/query_range'.format(host),
        params={'query': query, 'step': 1, 'end': end, 'start': start})

    body = response.json()
    results = body['data']['result']

    frames = list()
    for index, result in enumerate(results):
        metric = result['metric']
        values = result['values']
        df = pd.DataFrame(values, columns=['time', 'value'])
        for key in columns:
            df[key] = [metric[key]] * len(values)
        frames.append(df)
    
    return frames

def export_to_csv(metric, frames):
    pd.concat(frames).to_csv('./data/{}.csv'.format(metric['name']))

def export_to_image(metric, frames):
    df = pd.concat(frames)
    df = df.apply(pd.to_numeric, errors='ignore')
    
    df.plot(kind='line', x='time',y='value')
    plt.title(metric['description'])
    plt.xlabel('time (s)')
    plt.ylabel(metric['name'])
    plt.xticks(np.arange(min(df['index']), max(df['index'])+1, 1.0))

    plt.savefig('./data/{0}.png'.format(metric['name']))

def run_scenario(scenario):
    


if len(sys.argv) != 4:
    print('Usage: {0} metrics_file http://prometheus_host:9090 duration'.format(sys.argv[0]))
    sys.exit(1)

today = datetime.today()
metrics_file = sys.argv[1]
host = sys.argv[2]
duration = sys.argv[3]

with open(metrics_file) as file:
    metrics = yaml.load(file, Loader=yaml.FullLoader)
    end = datetime.timestamp(today)
    start = datetime.timestamp(today - timedelta(minutes=int(duration)))

    for metric in metrics['metrics']:
        frames = query_range(host, start, end, metric['query'], metric['columns'].split(','))
        if len(frames) > 0:
            template = '{}-{}'.format(today.strftime('%H-%M-%s-%d-%m'), metric['name'])
            export_to_csv(metric, frames)
            export_to_image(metric, frames)
            

