# HotelOps Executive Dashboard 🏨📊

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-UI-purple?style=for-the-badge&logo=flutter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

> **A centralized decision-support system for managing multi-property hotel portfolios in Australia.**

---

## 📸 Project Gallery

| View | Description |
| :--- | :--- |
| **Executive Overview** | Real-time tracking of **RevPAR**, **Occupancy**, and **Revenue**. Features a custom-built weekly trend chart and interactive data table with conditional formatting. |
| ![Overview Screenshot](https://github.com/yasinsd425-lab/Hotel-Dashboard-Flet/blob/main/Screenshot%202026-02-17%20181916.png) | |
| **System Architecture** | Visualizes the data pipeline from **Xero/Mews** (Source) to **Python** (Processing) and **Flet** (UI). Demonstrates understanding of full-stack data flow. |
| ![Architecture Screenshot](https://github.com/yasinsd425-lab/Hotel-Dashboard-Flet/blob/main/Screenshot%202026-02-17%20185428.png) | 
| ![Reports Screenshot](https://github.com/yasinsd425-lab/Hotel-Dashboard-Flet/blob/main/Screenshot%202026-02-17%20185402.png) | 
| ![Ops Screenshot](https://github.com/yasinsd425-lab/Hotel-Dashboard-Flet/blob/main/Screenshot%202026-02-17%20185417.png) | 

> *This application is designed for internal network deployment using Python/Flet.*

---

## 📖 Project Overview
This application addresses a common challenge in the hospitality industry: **Data Fragmentation**.
Managers often struggle to consolidate data from PMS (Property Management Systems), Accounting Software (Xero), and daily reports. 

**HotelOps Executive** solves this by providing a unified "Glass-morphism" interface that aggregates key metrics like **RevPAR**, **Occupancy Rates**, and **Net Operating Profit** in real-time.

### 🎯 Key Engineering Metrics
This is not just a UI wrapper; it implements core Industrial Engineering logic:
* **RevPAR (Revenue Per Available Room):** Calculated dynamically (`Total Revenue / Total Rooms`) to measure true efficiency beyond just raw income.
* **Occupancy Efficiency:** Real-time tracking of room utilization against targets.
* **Data Integrity Checks:** Automated flags for "Review Needed" or "Sync Errors" to ensure financial accuracy.

---

## 🏗 System Architecture
The application follows a modular data pipeline architecture:

```mermaid
graph TD
    A[Raw Data Sources] -->|JSON/API| B(Python Processing Engine)
    B -->|Cleaning & RevPAR Calc| C{Logic Layer}
    C -->|State Management| D[Flet UI Frontend]
    D -->|Executive View| E[User Dashboard]
