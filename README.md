
# Cyberdeck

**A custom Raspberry Pi 4-based portable computer for electronics, embedded systems development and robotics.**

> 🚧 **Work in Progress** — Currently in the design and development stage.

## Overview

The Cyberdeck is a personal engineering project focused on designing and building a **compact, self-contained portable computer** based on a Raspberry Pi 4.

The system combines a touchscreen, a compact wireless keyboard, a portable power system and a custom enclosure.

It is intended to serve as a versatile platform for **electronics, programming and future robotics projects**, while providing hands-on experience in hardware integration, power management and system design.

A custom **retrofuturistic graphical interface** is also being developed to provide quick access to system functions while maintaining the flexibility of a Linux desktop.

## Project Goals

- Build a compact, portable and self-contained Raspberry Pi computer.
- Integrate hardware components into a custom-designed enclosure.
- Develop a safe and reliable battery-powered system.
- Create a custom graphical interface optimized for a small touchscreen.
- Provide a platform for future electronics, embedded systems and robotics applications.

## Hardware

| Component | Selection | Status |
|-----------|-----------|--------|
| Main computer | Raspberry Pi 4 Model B | Selected |
| Display | Elecrow 5" Touchscreen (800×480) | Selected |
| Keyboard / Trackpad | Rii K06 Wireless | Selected |
| Battery | Li-ion / LiPo | Under consideration |
| Power Management | Battery protection + 5 V regulation | Under development |
| Cooling | Raspberry Pi heatsinks | Selected |
| Enclosure | Custom clamshell design | Under development |

Detailed component specifications and design decisions will be documented in [`docs/hardware.md`](docs/hardware.md).

## Software

The Cyberdeck is designed to run **Raspberry Pi OS**, providing access to a full Linux environment.

A custom graphical interface is being developed using **Python and Tkinter**.

The interface follows a minimal, retrofuturistic design inspired by classic computer terminals, optimized for the **800 × 480 touchscreen**.

Planned features include:

- System clock and date
- System monitoring
- Shutdown and power controls
- Navigation between system applications
- Access to the Raspberry Pi OS desktop

## System Architecture

The Cyberdeck integrates three main subsystems:

- **Computing:** Raspberry Pi 4 running Raspberry Pi OS.
- **Human-machine interface:** Touchscreen, wireless keyboard and custom GUI.
- **Power:** Rechargeable battery with protection and regulated power output.

Detailed system diagrams and technical documentation will be added as the design progresses.

## Future Applications

The Cyberdeck is being designed as a flexible platform for future personal engineering projects.

Potential applications include:

- Robot control and monitoring
- Telemetry visualization
- Embedded systems development
- Electronics testing and experimentation

These capabilities are long-term development goals and are not yet implemented.

## Development Progress

- [x] Define the project concept
- [x] Select the main computing platform
- [x] Select the display and input devices
- [x] Define the graphical interface concept
- [x] Define initial power requirements
- [ ] Finalize the power-management system
- [ ] Design the internal component layout
- [ ] Design and manufacture the enclosure
- [ ] Assemble and integrate the hardware
- [ ] Complete the graphical interface
- [ ] Perform system testing and validation

## Documentation

Technical documentation will be organized in the [`docs/`](docs/) directory as development progresses.

| Document | Description |
|----------|-------------|
| [Hardware](docs/hardware.md) | Components, specifications and hardware selection |
| [Power System](docs/power-system.md) | Battery selection, power management and electrical design |
| [System Design](docs/system-design.md) | System architecture, integration and enclosure design |
| [Development Log](docs/development-log.md) | Engineering decisions, tests and development progress |

Documentation will be added progressively as each part of the project is developed.

---

*Personal engineering project focused on electronics, embedded systems and hands-on learning.*
