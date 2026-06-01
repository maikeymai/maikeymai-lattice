
# Lattice Architecture

## Overview

Lattice is a six-sled ARM infrastructure platform designed to explore the architecture and operational concepts behind modern infrastructure systems.

---

## Physical Architecture

```text
DeskPi Super6C

├── sled-01
├── sled-02
├── sled-03
├── sled-04
├── sled-05
└── sled-06
```

Each sled consists of:

- Raspberry Pi Compute Module 4
- Samsung 980 NVMe SSD

---

## Logical Architecture

```text
Dashboard
    │
    ▼
Lattice Controller
    │
    ▼
Telemetry Agents
    │
    ▼
Compute Sleds
```

---

## Planned Components

### Lattice Controller

The controller will provide:

- Inventory Management
- Telemetry Collection
- Health Monitoring
- Topology Visualization

### Telemetry Agent

Each sled will run an agent responsible for:

- Temperature Reporting
- Storage Reporting
- Memory Reporting
- System Health Reporting

### Storage Layer

The storage layer will provide:

- Distributed Storage
- Capacity Reporting
- Replication
- Snapshot Management

### Observability Platform

The observability platform will provide:

- Metrics
- Logging
- Dashboards
- Alerting
