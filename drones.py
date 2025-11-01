import pybullet as p
import pybullet_data
import numpy as np
import cv2
import time
import os
import random
p.connect(p.GUI)
p.setGravity(0, 0, -9.8)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.resetDebugVisualizerCamera(cameraDistance=15, cameraYaw=45, cameraPitch=-40, cameraTargetPosition=[0, 0, 2])
p.setAdditionalSearchPath(pybullet_data.getDataPath())
plane_id = p.loadURDF("plane.urdf")
p.changeVisualShape(plane_id, -1, rgbaColor=[0.03, 0.03, 0.05, 1])
image_files = ["pikachu.png", "charmendor.png", "charmelon.png","charizard.png","bulbasur.png","ivysur.png","sqartle.png"]

def extract_positions_from_image(image_file, num_points=400, scale=0.035):
    if not os.path.exists(image_file):
        print(f"⚠️ {image_file} not found!")
        return []
    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (300, 300))
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ys, xs = np.nonzero(thresh)
    coords = list(zip(xs, ys))
    if len(coords) > num_points:
        idx = np.linspace(0, len(coords) - 1, num_points, dtype=int)
        coords = [coords[i] for i in idx]
    return [[(x - 150) * scale, -(y - 150) * scale, 2] for x, y in coords]


num_drones = 400
drones = []
for _ in range(num_drones):
    sphere = p.createVisualShape(p.GEOM_SPHERE, radius=0.06, rgbaColor=[1, 1, 0, 1])
    drone_id = p.createMultiBody(baseMass=0, baseVisualShapeIndex=sphere, basePosition=[0, 0, 5])
    drones.append(drone_id)


start_positions = [[random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(3, 6)] for _ in range(num_drones)]


def transition_to_shape(target_positions, steps=400, delay=0.02):
    global start_positions
    while len(target_positions) < num_drones:
        target_positions.append([random.uniform(-5, 5), random.uniform(-5, 5), 5])
    for step in range(steps):
        t = (step + 1) / steps
        for i, drone_id in enumerate(drones):
            start = start_positions[i]
            target = target_positions[i]
            new_pos = [
                start[0] * (1 - t) + target[0] * t,
                start[1] * (1 - t) + target[1] * t,
                start[2] * (1 - t) + target[2] * t
            ]
            p.resetBasePositionAndOrientation(drone_id, new_pos, [0, 0, 0, 1])
        p.stepSimulation()
        time.sleep(delay)
    start_positions = target_positions.copy()

try:
    cycle = 0
    while True:
        for image in image_files:
            print(f"🚀 Transitioning to {image}...")
            targets = extract_positions_from_image(image, num_drones)
            if not targets:
                continue
            transition_to_shape(targets, steps=400, delay=0.025)
            print(f"✨ Holding {image} shape...")
            for t in range(300):
                r = 0.5 + 0.5 * np.sin(0.03 * (t + cycle))
                g = 0.5 + 0.5 * np.sin(0.03 * (t + cycle) + 2 * np.pi / 3)
                b = 0.5 + 0.5 * np.sin(0.03 * (t + cycle) + 4 * np.pi / 3)
                for drone_id in drones:
                    p.changeVisualShape(drone_id, -1, rgbaColor=[r, g, b, 1])
                p.stepSimulation()
                time.sleep(0.02)
            cycle += 1

except KeyboardInterrupt:
    p.disconnect()
