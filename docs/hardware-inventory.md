
# Hardware Inventory

## Overview

Lattice is built on a DeskPi Super6C platform using six Raspberry Pi Compute Module 4 nodes and six Samsung 980 NVMe SSDs.

---

## Platform

| Component | Description |
|------------|------------|
| Chassis | DeskPi Super6C |
| Compute Nodes | 6x Raspberry Pi Compute Module 4 |
| Storage | 6x Samsung 980 NVMe SSD |
| Capacity | 1TB per node |
| Total Raw Capacity | 6TB |

---

## Sled Inventory

| Sled | Compute | Storage |
|--------|----------|---------|
| sled-01 | CM4 | Samsung 980 1TB |
| sled-02 | CM4 | Samsung 980 1TB |
| sled-03 | CM4 | Samsung 980 1TB |
| sled-04 | CM4 | Samsung 980 1TB |
| sled-05 | CM4 | Samsung 980 1TB |
| sled-06 | CM4 | Samsung 980 1TB |

---

## Node Inventory

| Sled | Hostname | Static IP | OS | Storage |
|---|---|---|---|---|
| 1 | sled-01 | 192.168.68.101 | Ubuntu Server 24.04 LTS | Samsung 980 1TB NVMe |
| 2 | sled-02 | 192.168.68.102 | Ubuntu Server 24.04 LTS | Samsung 980 1TB NVMe |
| 3 | sled-03 | 192.168.68.103 | Ubuntu Server 24.04 LTS | Samsung 980 1TB NVMe |
| 4 | sled-04 | 192.168.68.104 | Ubuntu Server 24.04 LTS | Samsung 980 1TB NVMe |
| 5 | sled-05 | 192.168.68.105 | Ubuntu Server 24.04 LTS | Samsung 980 1TB NVMe |
| 6 | sled-06 | 192.168.68.106 | Ubuntu Server 24.04 LTS | Samsung 980 1TB NVMe |

---

## Networking

Current Status:

- Cluster assembly complete
- Operating system installation pending
- Network configuration pending

---

## Notes

The platform is intended to explore rack-scale infrastructure concepts including:

- Platform Engineering
- Infrastructure Automation
- Distributed Storage
- Observability
- Control Plane Design
