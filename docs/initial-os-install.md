# Initial Operating System Installation

## Overview

This document tracks the initial operating system deployment for the Lattice platform.

Lattice is a six-node ARM infrastructure platform built on a DeskPi Super6C utilizing Raspberry Pi Compute Module 4 hardware and Samsung 980 NVMe storage.

---

## Objective

Deploy Ubuntu Server 24.04 LTS to the first compute sled and establish a repeatable installation process for the remaining nodes.

---

## Hardware Configuration

### Platform

* DeskPi Super6C

### Compute

* Raspberry Pi Compute Module 4
* eMMC Storage

### Storage

* Samsung 980 NVMe SSD
* 1TB Capacity

---

## Initial Installation Attempt

The initial deployment strategy utilized a microSD card containing Ubuntu Server 24.04 LTS.

### Result

The Compute Module repeatedly entered the Raspberry Pi bootloader and cycled through available boot devices without successfully locating a bootable operating system.

### Observation

The bootloader remained active and continuously searched for a valid operating system image.

---

## Root Cause

Review of the DeskPi Super6C documentation identified that Compute Module 4 systems equipped with eMMC storage are intended to be imaged directly through USB boot mode.

The installation process requires the Compute Module to expose its onboard eMMC storage to a host workstation for operating system deployment.

---

## Revised Deployment Method

### Operating System

Ubuntu Server 24.04 LTS (64-bit)

### Deployment Workflow

1. Enable Compute Module USB boot mode.
2. Connect the DeskPi Super6C USB slave interface to a macOS workstation.
3. Launch Raspberry Pi Imager.
4. Detect Compute Module eMMC storage.
5. Configure deployment settings:

   * Hostname: sled-01
   * Username: michael
   * SSH Enabled
6. Write Ubuntu Server image directly to eMMC.
7. Verify image deployment.
8. Remove USB boot mode.
9. Boot normally from eMMC.

---

## Current Status

### Completed

* [x] Hardware assembly
* [x] Compute Module installation
* [x] Samsung 980 NVMe installation
* [x] Ubuntu image deployment to eMMC

### Completed

* [x] First successful operating system boot
* [x] SSH validation
* [x] NVMe validation

### In Progess

* [x] Static IP assignment
* [x] Operating system baseline configuration
* [ ] Ansible inventory creation
* [ ] Cluster node deployment

---

## Lessons Learned

The DeskPi Super6C deployment process differs from traditional Raspberry Pi systems.

While microSD deployment is possible in some configurations, the preferred deployment workflow for Compute Module 4 systems with onboard eMMC is direct imaging through USB boot mode.

Understanding the carrier board architecture and boot process significantly reduces troubleshooting time during initial deployment.

---

## Bring-Up Results

The initial node deployment process was validated and repeated across the Super6C platform.

Each sled was imaged directly to CM4 eMMC using USB boot mode and configured with:

- Ubuntu Server 24.04 LTS
- SSH enabled
- Static IP addressing
- Samsung 980 NVMe detected
- Baseline package updates

## Validated Node

```text
sled-01
Ubuntu Server 24.04 LTS
Kernel: 6.8.0-1047-raspi
Architecture: aarch64
Memory: 8GB
eMMC: 32GB
NVMe: Samsung SSD 980 1TB

1. Validate successful Ubuntu boot.
2. Verify hostname configuration.
3. Validate SSH connectivity.
4. Verify Samsung 980 NVMe detection.
5. Document node inventory.
6. Repeat deployment process for remaining sleds.
