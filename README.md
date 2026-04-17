# SDN Static Routing using POX and Mininet
## Problem Statement
This project implements static routing in a Software Defined Networking (SDN) environment using a POX controller and Mininet. The controller installs flow rules manually to control packet forwarding behavior.
---
## Tools Used
* Mininet
* POX Controller
* OpenFlow Protocol
* iperf
* ping
---
## 🌐 Network Topology
h1 --- s1 --- s2 --- h2
---
## ⚙️ Setup Instructions
1. Install Mininet:
   sudo apt install mininet -y
2. Clone POX:
   git clone https://github.com/noxrepo/pox.git
   cd pox
3. Run Controller:
   ./pox.py static_routing
4. Run Mininet:
   sudo mn --custom topology.py --topo static --controller=remote
---
## 🚀 Execution Steps
* Start the POX controller
* Start Mininet
* Run pingall
* Check flow table using dpctl dump-flows
* Run iperf for throughput
---
## 📊 Results
### Scenario 1: Normal Routing
* pingall shows 0% packet loss
### Scenario 2: Blocked Traffic
* pingall shows 100% packet loss
---
## 📸 Screenshots
### Screenshot 1: Mininet Setup
<img width="556" height="525" alt="screenshot 1 " src="https://github.com/user-attachments/assets/c1110284-47f0-4d90-9f4e-5c052e189566" />

### Screenshot 2: POX Controller
<img width="727" height="300" alt="screenshot 2" src="https://github.com/user-attachments/assets/c3b5e522-656a-457c-bcd3-c1b670a4a136" />

### Screenshot 3: Connectivity and Flow table 
<img width="728" height="290" alt="scnreenshot 3" src="https://github.com/user-attachments/assets/6cde8ea9-bdea-4edc-9ccd-ee3088a0460e" />

### Screenshot 4: Performance
<img width="969" height="204" alt="screenshot 5 " src="https://github.com/user-attachments/assets/e5e9151f-cf6c-4d0c-8070-66f6b209453c" />

### Screenshot 5: Normal Scenario
<img width="373" height="105" alt="screenshot 6 " src="https://github.com/user-attachments/assets/c31a4015-4db1-4b51-a6bf-64c2464274e4" />

### Screenshot 6: Blocked Scenario
<img width="410" height="196" alt="screenshot 7" src="https://github.com/user-attachments/assets/49b4a8aa-03d1-4ea7-9375-31a466702011" />
---
## 📈 Performance Analysis
Latency is measured using ping and throughput using iperf.
---
## ✅ Conclusion
This project demonstrates how SDN controllers manage network behavior using static flow rules.
---
## 📚 References
* Mininet Documentation
* POX Documentation

