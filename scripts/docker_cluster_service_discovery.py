#!/usr/bin/python3

import argparse
import docker

class SwarmInspect:
    def __init__(self, args):
        self.args = args
        self.cli = docker.from_env()

    def discovery_services(self):
        services_list = self.cli.services.get(self.args.name)
        attrs = services_list.attrs
        max_replicas = int(attrs['Spec']['Mode']['Replicated']['Replicas']) # number of replicas for a service
        running_replicas = len([task for task in services_list.tasks() if task['Status']['State'] == 'running']) # the number of running tasks for a service
        if running_replicas >= max_replicas & running_replicas > 0:
            print(1)
        else:
            print(0)
        # print(attrs['Spec']['Mode']['Replicated']['Replicas'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, required=True)
    args = parser.parse_args()
    
    swarmInspect = SwarmInspect(args=args)
    swarmInspect.discovery_services()
            

