# Technology Decisions

## Philosophy

Lattice intentionally uses open-source software to learn the architectural concepts behind modern infrastructure platforms.

The objective is understanding systems rather than consuming managed services.

---

## Operating System

### Selected

Ubuntu Server 24.04 LTS

### Alternatives Considered

- Talos Linux
- Raspberry Pi OS
- Debian

### Reason

Ubuntu provides excellent ARM support and a large ecosystem while remaining easy to manage during initial development.

---

## Cluster Platform

### Selected

k3s

### Enterprise Equivalent

OpenShift

### Reason

k3s provides a lightweight Kubernetes implementation well suited to ARM hardware.

---

## Storage

### Selected

Longhorn

### Enterprise Equivalent

VMware vSAN

### Reason

Longhorn provides distributed storage concepts without requiring enterprise licensing.

---

## Observability

### Selected

Prometheus
Grafana
Loki

### Enterprise Equivalents

Datadog
Splunk
Dynatrace

### Reason

The open-source observability stack provides visibility into metrics, logs, and system health while remaining fully self-hosted.

---

## Configuration Management

### Selected

Ansible

### Enterprise Equivalent

Red Hat Ansible Automation Platform

### Reason

Ansible allows repeatable configuration management and aligns with existing professional experience.

---

## Future Evaluation

Future technologies under consideration include:

- Talos Linux
- Ceph
- MinIO
- Authentik
- WireGuard
