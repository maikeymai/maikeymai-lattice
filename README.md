# Lattice

> A six-sled ARM infrastructure platform for studying rack-scale systems concepts.

## Overview

Lattice is a Compute Module 4 based infrastructure lab built to explore the architectural and operational concepts behind modern cloud appliance platforms.

The project focuses on:

- Orchestration
- Infrastructure automation
- Distributed storage
- Observability
- Cluster operations
- Control plane design

---

## Hardware

### Platform

- DeskPi Super6C

### Compute

- 6x Raspberry Pi Compute Module 4

### Storage

- 6x Samsung 980 NVMe SSD
- 1TB per sled
- 6TB raw capacity

---

## Sled Layout

```text
sled-01
sled-02
sled-03
sled-04
sled-05
sled-06
```

---

## Project Goals

- Reproducible infrastructure
- Observability-first operations
- Automated deployment workflows
- Centralized fleet management
- Storage replication
- Infrastructure documentation

## Documentation

- [Architecture](docs/architecture.md)
- [Hardware Inventory](docs/hardware-inventory.md)
- [Technology Decisions](docs/technology-decisions.md)
- [Roadmap](docs/roadmap.md)
- [Initial OS Installation](docs/initial-os-install.md)

## Roadmap

### Phase 1

- [x] Hardware assembly
- [ ] Ubuntu deployment
- [ ] SSH access
- [ ] Static IP configuration

### Phase 2

- [ ] Ansible automation
- [ ] Inventory management
- [ ] Hardware telemetry

### Phase 3

- [ ] Lattice Controller
- [ ] Fleet API
- [ ] Dashboard

### Phase 4

- [ ] Kubernetes
- [ ] Longhorn
- [ ] Prometheus
- [ ] Grafana

---

## Open Source Technology Choices

| Open Source | Enterprise Equivalent |
|------------|----------------------|
| Ubuntu Server | Red Hat Enterprise Linux |
| k3s | OpenShift |
| Longhorn | VMware vSAN |
| Prometheus | Datadog |
| Grafana | Grafana Enterprise |
| Loki | Splunk |
| MinIO | AWS S3 |
| Authentik | Okta |

The objective is to understand the underlying systems and operational models while using free and open-source software.
