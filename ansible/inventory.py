#!/usr/bin/env python

import argparse
import netifaces
import os
import json


class GlusterFSInventory:
    def __init__(self, iface):
        slash24 = self.get_subnet(iface)

        self.vol1 = {
            'hosts': ['%s.11' % slash24],
            'vars': {
                'ansible_ssh_user': 'vagrant',
                'ansible_ssh_private_key_file': '.vagrant/machines/vol1/virtualbox/private_key',
                'gluster_volume_disks': []
            }
        }

        self.vol2 = {
            'hosts': ['%s.12' % slash24],
            'vars': {
                'ansible_ssh_user': 'vagrant',
                'ansible_ssh_private_key_file': '.vagrant/machines/vol2/virtualbox/private_key',
                'gluster_volume_disks': []
            }
        }

        self.vol3 = {
            'hosts': ['%s.13' % slash24],
            'vars': {
                'ansible_ssh_user': 'vagrant',
                'ansible_ssh_private_key_file': '.vagrant/machines/vol3/virtualbox/private_key',
                'gluster_volume_disks': []
            }
        }

    def get_subnet(self, iface):
        iface_addr = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
        return '.'.join(iface_addr.split('.')[:-1])

    def list(self):
        return {
            'vol1': self.vol1,
            'vol2': self.vol2,
            'vol3': self.vol3
        }


def read_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store')
    return parser.parse_args()


def main():
    iface = os.environ['VAGRANT_BRIDGE_IFACE']
    if iface == '':
        raise 'VAGRANT_BRIDGE_IFACE required'

    inventory = GlusterFSInventory(iface)

    args = read_cli_args()
    if args.list:
        print(json.dumps(inventory.list()))
    elif args.host:
        print('{}')


if __name__ == '__main__':
    main()
