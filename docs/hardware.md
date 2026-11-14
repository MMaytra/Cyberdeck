
# Hardware Documentation

This document describes the hardware components, specifications and integration considerations of the **Cyberdeck** project.

The system is based on a Raspberry Pi 4 Model B and combines a touchscreen, wireless input devices, a portable power supply and a custom enclosure.

The hardware configuration is still evolving. This document will be updated as components are selected, integrated and tested.

---

## 1. System Overview

The Cyberdeck is designed as a compact, self-contained portable computer for electronics, programming and future robotics applications.

The hardware is divided into the following subsystems:

- **Computing:** Main processing platform.
- **Display:** Visual output and touchscreen interaction.
- **Input:** Keyboard and pointing device.
- **Power:** Rechargeable battery, protection and voltage regulation.
- **Cooling:** Thermal management of the Raspberry Pi.
- **Enclosure:** Mechanical integration and protection.

### System Architecture

A general hardware architecture diagram will be added as the design progresses.

<!-- IMAGE PLACEHOLDER: System architecture diagram -->
<!-- ![System Architecture](../images/design/system-architecture.png) -->

---

## 2. Main Computing Platform

### Raspberry Pi 4 Model B

**Status:** Selected

The Raspberry Pi 4 Model B acts as the central processing unit of the Cyberdeck.

It is responsible for running the operating system, executing applications, managing the graphical interface and communicating with external hardware.

### Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| Model | Raspberry Pi 4 Model B |
| Processor | Broadcom BCM2711 |
| CPU | Quad-core ARM Cortex-A72, 1.8 GHz |
| RAM | Depends on selected board variant |
| GPIO | 40-pin header |
| USB | 2 × USB 3.0, 2 × USB 2.0 |
| Video output | 2 × Micro-HDMI |
| Wireless connectivity | Wi-Fi and Bluetooth |
| Storage | MicroSD |
| Power input | USB-C, 5.1 V / 3 A recommended |

### Integration Considerations

The Raspberry Pi must be positioned inside the enclosure to:

- Allow access to the necessary connectors.
- Provide sufficient space for internal wiring.
- Support adequate heat dissipation.
- Allow secure mechanical mounting.
- Minimize the overall dimensions of the system.

### Component Image

<!-- IMAGE PLACEHOLDER: Raspberry Pi 4 -->
<!-- ![Raspberry Pi 4](../images/hardware/raspberry-pi-4.jpg) -->

**Documentation:**
[Raspberry Pi Official Documentation](https://www.raspberrypi.com/documentation/)

---

## 3. Display

### Elecrow 5-inch Touchscreen

**Status:** Selected

The Cyberdeck uses a compact touchscreen as its primary display and graphical interaction device.

The small screen size is one of the main constraints influencing the enclosure design and user interface.

### Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| Manufacturer | Elecrow |
| Display size | 5 inches |
| Resolution | 800 × 480 px |
| Touch functionality | Yes |
| Video interface | To be verified for exact model |
| Touch interface | To be verified for exact model |
| Power requirements | To be verified |

### Integration Considerations

The display must be integrated into the enclosure while considering:

- Screen visibility and viewing angle.
- Accessibility of the touchscreen.
- Available space for connectors and cables.
- Mechanical mounting and protection.
- Display power consumption.

The custom graphical interface is being designed specifically for the native resolution of **800 × 480 pixels**.

### Component Image

<!-- IMAGE PLACEHOLDER: Elecrow touchscreen -->
<!-- ![Elecrow Display](../images/hardware/elecrow-display.jpg) -->

### References

- Exact product link: TBD
- Datasheet / installation instructions: TBD

---

## 4. Input Devices

### Rii K06 Wireless Keyboard / Trackpad

**Status:** Selected

A Rii K06 wireless mini keyboard with integrated trackpad is used as the main physical input device.

The compact design provides both text input and pointer control without requiring a separate mouse.

### Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| Model | Rii K06 |
| Input type | Keyboard + trackpad |
| Wireless technology | 2.4 GHz |
| Connection | USB receiver |
| Power | Internal rechargeable battery (verify exact variant) |

### Integration Considerations

The input system must allow:

- Comfortable typing and cursor navigation.
- Reliable communication with the Raspberry Pi.
- Compact storage and transport.
- Easy access during system operation.

The dedicated USB receiver avoids the need to configure Bluetooth pairing.

### Component Image

<!-- IMAGE PLACEHOLDER: Rii K06 keyboard -->
<!-- ![Rii K06](../images/hardware/rii-k06.jpg) -->

### References

- Product documentation: TBD

---

## 5. Power System

**Status:** Under development

The Cyberdeck requires a portable power system capable of supplying the Raspberry Pi and the remaining hardware.

The current design focuses on rechargeable lithium-based batteries combined with protection circuitry and regulated power conversion.

### Initial Requirements

| Parameter | Requirement |
|-----------|-------------|
| Output voltage | Regulated 5 V |
| Output current | At least 3 A (initial target) |
| Battery type | Li-ion / LiPo |
| Battery configuration | 1S preferred concept |
| Target capacity | 5000–10000 mAh |
| Maximum dimensions | Approximately 100 × 90 × 20 mm |
| Target budget | ≤ €40 |
| Rechargeable | Yes |
| Protection | Overcharge, over-discharge, overcurrent and short-circuit |
| UPS / power-path | Preferred |

The final power requirements must account for the combined consumption of the Raspberry Pi, touchscreen and connected peripherals.

### Current Design Concept

The preferred solution under consideration consists of:

1. A flat rechargeable Li-ion/LiPo battery.
2. Battery protection circuitry.
3. A DC-DC boost converter providing a regulated 5 V output.
4. A suitable charging and power-management system.

The final configuration has not yet been selected or validated.

### Component Images

<!-- IMAGE PLACEHOLDER: Battery -->
<!-- ![Battery](../images/hardware/battery.jpg) -->

<!-- IMAGE PLACEHOLDER: Power-management module -->
<!-- ![Power Management](../images/hardware/power-module.jpg) -->

### Technical Documentation

Detailed calculations, component comparisons, electrical diagrams and test results will be documented in:

[Power System Documentation](power-system.md)

---

## 6. Cooling

### Raspberry Pi Heatsinks

**Status:** Selected

Passive heatsinks have been selected as the initial thermal-management solution.

Their purpose is to improve heat dissipation from the Raspberry Pi during operation.

### Design Considerations

- Available internal airflow.
- Clearance between heatsinks and enclosure.
- CPU temperature under sustained load.
- Thermal behavior during battery-powered operation.

The final thermal configuration will be evaluated during system testing.

Active cooling may be considered if passive cooling proves insufficient.

### Component Image

<!-- IMAGE PLACEHOLDER: Raspberry Pi with heatsinks -->
<!-- ![Cooling System](../images/hardware/cooling.jpg) -->

---


## 7. Enclosure & Mechanical Integration

**Status:** Under development

The Cyberdeck uses a **commercial Forever Young bag** as its main enclosure, rather than a fully custom-manufactured housing.

This approach reduces manufacturing complexity while providing a compact and portable structure for the system.

Custom 3D-printed components are being designed to integrate the display and keyboard into the existing enclosure.

### Main Enclosure

| Parameter | Specification |
|-----------|---------------|
| Manufacturer | Forever Young |
| Enclosure type | Commercial bag |
| Structural approach | Modified existing enclosure |
| Custom components | 3D-printed mounting frames |
| Manufacturing method | FDM 3D printing |
| Material | TBD |
| Mounting system | Under development |

### Enclosure Image

<!-- IMAGE PLACEHOLDER: Forever Young bag -->
<!-- ![Main Enclosure](../images/design/forever-young-bag.jpg) -->

### 3D-Printed Display Frame

A custom frame is being designed to integrate the Elecrow 5-inch touchscreen into the enclosure.

The frame is intended to:

- Provide a clean and secure display mounting.
- Conceal the rear of the display and its electronics.
- Improve the overall appearance of the assembly.
- Allow suitable cable routing.
- Facilitate installation and maintenance.

#### Display Frame Design

<!-- IMAGE PLACEHOLDER: Display frame CAD render -->
<!-- ![Display Frame](../images/design/display-frame.png) -->

### 3D-Printed Keyboard Frame

A second custom frame is being designed to integrate the Rii K06 keyboard and trackpad.

The frame is intended to:

- Securely position the keyboard.
- Conceal the rear of the keyboard and surrounding installation.
- Provide a clean and consistent appearance.
- Maintain access to the keyboard controls.
- Allow easy installation and removal when necessary.

#### Keyboard Frame Design

<!-- IMAGE PLACEHOLDER: Keyboard frame CAD render -->
<!-- ![Keyboard Frame](../images/design/keyboard-frame.png) -->

### Mechanical Integration

The main mechanical challenge is adapting the electronic components to the available space and geometry of the existing bag.

Key design considerations include:

- Internal dimensions and component clearances.
- Secure attachment of the 3D-printed frames.
- Display and keyboard alignment.
- Cable routing between the two sections.
- Accessibility for maintenance.
- Protection of electronic components.
- Adequate ventilation and heat dissipation.

### Assembly

<!-- IMAGE PLACEHOLDER: Mechanical assembly -->
<!-- ![Mechanical Assembly](../images/progress/mechanical-assembly.jpg) -->

Further mechanical design details will be documented in:

[System Design Documentation](system-design.md)


## 8. Hardware Integration

This section will document the physical and electrical integration of the different subsystems.

### Planned Integration Tasks

- Confirm display connections and power requirements.
- Define power distribution between components.
- Verify USB receiver placement and available ports.
- Define internal cable routing.
- Design mechanical mounting points.
- Verify connector accessibility.
- Evaluate electrical and thermal performance.

### Integration Images

<!-- IMAGE PLACEHOLDER: Internal assembly -->
<!-- ![Hardware Assembly](../images/progress/hardware-assembly.jpg) -->

<!-- IMAGE PLACEHOLDER: Completed internal wiring -->
<!-- ![Internal Wiring](../images/progress/internal-wiring.jpg) -->

---

## 9. Component Summary

| Component | Model / Selection | Status |
|-----------|-------------------|--------|
| Main computer | Raspberry Pi 4 Model B | Selected |
| Display | Elecrow 5" Touchscreen | Selected |
| Keyboard / Trackpad | Rii K06 | Selected |
| Battery | Flat Li-ion / LiPo | Under consideration |
| Power management | Protected battery + DC-DC regulation | Under development |
| Cooling | Passive heatsinks | Selected |
| Enclosure | Custom clamshell | Under development |

Component status will be updated as the project progresses.

---

## 10. References

Technical documentation and manufacturer resources:

1. [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
2. Elecrow display documentation — TBD
3. Rii K06 product documentation — TBD
4. Battery datasheet — TBD
5. Power-management module datasheet — TBD

---

*This document is part of the Cyberdeck engineering documentation and will be updated throughout the development process.*
