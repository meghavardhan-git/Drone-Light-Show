# 🚁 Drone Light Show Simulation using PyBullet

## 📘 Overview
This project demonstrates a **Drone Light Show Simulation** built using the **PyBullet physics engine**.  
It visualizes how multiple drones can move in coordinated patterns to form artistic shapes, text, or animations — similar to real-world drone light shows used in celebrations, sports events, and tech demonstrations.

The main focus of this project is on **formation control**, **synchronized movement**, and **smooth trajectory transitions** between formations.

---

## 🎯 Objectives
- Simulate multiple drones in a 3D environment using PyBullet.  
- Create and visualize **formation transitions** (e.g., circle → heart → text).  
- Demonstrate **synchronized, collision-free flight** behavior.  
- Provide a foundation for testing swarm coordination before real drone deployment.

---

## 🧠 Key Features
- 🪶 **Physics-based simulation** with gravity and drone mass models.  
- 💡 **Multiple drone coordination** — configurable number of drones.  
- 🌈 **Dynamic light effects** — colored spheres represent drones.  
- 🔄 **Smooth shape transitions** between predefined formations.  
- ⚙️ **Fully customizable** parameters for altitude, speed, spacing, and formations.



---

## ⚙️ Technologies Used
| Component | Description |
|------------|-------------|
| **Python 3.10+** | Core programming language |
| **PyBullet** | Physics simulation engine |
| **NumPy** | Vectorized mathematical operations |
| **Matplotlib (optional)** | Visualization of paths or data |
| **URDF (Unified Robot Description Format)** | Drone model definition |

---

## 🚀 Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Drone-Light-Show.git
cd Drone-Light-Show
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Simulation
```bash
python drones.py
```

---



## 🕹️ Controls
| Key | Action |
|-----|---------|
| `R` | Reset simulation |
| `Q` | Quit simulation |
| `Space` | Pause / Resume animation |
| `↑ / ↓` | Increase / Decrease altitude |
| `← / →` | Change formation pattern |

---

## 🎨 Visualization
Each drone is represented by a small **colored sphere** with a glowing effect to simulate light.  
The drones move in a synchronized manner to create smooth transitions between patterns such as:
- Pokemon Transitions
You can also adjust:
- Drone count  
- Altitude  
- Transition duration  
- Color schemes  

---

## 🧠 Simulation Logic
1. Initialize simulation in PyBullet.  
2. Spawn multiple drone objects (URDF models or simple spheres).  
3. Assign each drone a target position from a formation pattern.  
4. Interpolate positions frame-by-frame for smooth motion.  
5. Switch formations periodically or via keyboard input.  
6. Render scene in real-time 3D viewer.



---

## 🧪 Future Enhancements
- Add **drone dynamics** using PID controllers.  
- Implement **collision avoidance** algorithms (e.g., boids, potential fields).  
- Enable **real-time control** via keyboard or network.  
- Export flight paths for **real drone swarm execution**.  
- Add **text-based formation generation** (e.g., displaying letters or words).  

---

## 🧭 References
- [PyBullet Documentation](https://pybullet.org/wordpress/)
- [URDF Format Reference](https://wiki.ros.org/urdf)
- [Formation Control Algorithms](https://arxiv.org/)
- [Swarm Robotics Concepts](https://ieeexplore.ieee.org/)

---

## 👨‍💻 Author
**Your Name**  
📧 meghavardhan2212@gmail.com  
🔗 [https://github.com/meghavardhan-git](https://github.com/meghavardhan-git)

---

## 📄 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 💬 Acknowledgements
Special thanks to the **PyBullet community** and open-source contributors for enabling easy simulation of robotics and drone physics in Python.
