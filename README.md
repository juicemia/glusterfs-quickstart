# GlusterFS Quick Start

**STATUS:** Right now this repo automates up to step two of the GlusterFS quick start guide.

This repo bootstraps a GlusterFS cluster using Vagrant and Ansible, following the steps shown
in the GlusterFS Quick Start guide.

## Prerequisites

Make sure you have `python3` and `python3-pip` installed. Then, install `virtualenv`.

```
$: python3 -m pip install --upgrade virtualenv
```

Once you have that done, initialize the virtual environment for this repo.

```
$: python3 -m virtualenv venv
$: source venv/bin/activate
$: pip install -r requirements.txt
```

## Quick Start

```
$: source venv/bin/activate
$: VAGRANT_BRIDGE_IFACE=$YOUR_NETWORK_INTERFACE vagrant up
$: VAGRANT_BRIDGE_IFACE=$YOUR_NETWORK_INTERFACE ansible-playbook -i ansible/inventory.py ansible/setup-glusterfs.yml
```