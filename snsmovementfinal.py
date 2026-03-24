#!/usr/bin/env python3
import os
import sys
import time
import tkinter as tk
from tkinter import ttk

# Add SDK to path
sys.path.append(r"C:\Users\Ray\Desktop\snsmultirobo final\xArm-Python-SDK")
from xarm.wrapper import XArmAPI

# Connect to arm
ip = "192.168.1.204"
arm = XArmAPI(ip, is_radian=True)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

# Create window
window = tk.Tk()
window.title('Robot Movement Control')
window.geometry('400x600')

# Scrollable frame
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

button_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=button_frame, anchor="nw")


# ============================================
# ADD YOUR MOVEMENT FUNCTIONS HERE
# ============================================

def movement1():
    arm.load_trajectory('movement1.traj')
    arm.playback_trajectory()
    arm.playback_trajectory(wait=True)


def movement2():
    arm.load_trajectory('movement2.traj')
    arm.playback_trajectory()
    arm.playback_trajectory(wait=True)


def halfbreathing1():
    pass
    for i in range(int(1)):
        #####breathing#####

        arm.set_servo_angle(angle=[-6, -89, -66.5, 12, 88, -1.9, 0.0], speed=1.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.set_servo_angle(angle=[-4, -92, -68, 8, 91, -1.9, 0.0], speed=2.5, mvacc=200, raidus=30,
                            is_radian=False, wait=False)
        arm.playback_trajectory(wait=True)


def breathing1():
    pass
    for i in range(int(1)):
        #####breathing#####

        arm.set_servo_angle(angle=[-6, -89, -63.5, 12, 88, -1.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.set_servo_angle(angle=[-6, -87, -68.5, 12, 85, 3.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.playback_trajectory(wait=True)


def breathing2():
    pass
    for i in range(int(2)):
        #####breathing#####

        arm.set_servo_angle(angle=[-6, -89, -63.5, 12, 88, -1.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.set_servo_angle(angle=[-6, -87, -68.5, 12, 85, 3.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.playback_trajectory(wait=True)


def breathing3():
    pass
    for i in range(int(3)):
        #####breathing#####

        arm.set_servo_angle(angle=[-6, -89, -63.5, 12, 88, -1.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.set_servo_angle(angle=[-6, -87, -68.5, 12, 85, 3.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.playback_trajectory(wait=True)


def breathing4():
    pass
    for i in range(int(5)):
        #####breathing#####

        arm.set_servo_angle(angle=[-6, -89, -63.5, 12, 88, -1.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.set_servo_angle(angle=[-6, -87, -68.5, 12, 85, 3.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.playback_trajectory(wait=True)


def breathing5():
    pass
    for i in range(int(8)):
        #####breathing#####

        arm.set_servo_angle(angle=[-6, -89, -63.5, 12, 88, -1.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.set_servo_angle(angle=[-6, -87, -68.5, 12, 85, 3.9, 0.0], speed=3.5, mvacc=500, raidus=30,
                            is_radian=False, wait=False)
        arm.playback_trajectory(wait=True)
def analyze():
    arm.load_trajectory('analyze.traj')
    arm.playback_trajectory()
    arm.playback_trajectory(wait=True)

def takeover():
    arm.load_trajectory('takeover.traj')
    arm.playback_trajectory()
    arm.playback_trajectory(wait=True)

def wire1():
    arm.load_trajectory('wire1.traj')
    arm.playback_trajectory()
    arm.playback_trajectory(wait=True)

def wire2():
    arm.load_trajectory('wire2.traj')
    arm.playback_trajectory()
    arm.playback_trajectory(wait=True)
# Add more here!
def wire3():
    arm.load_trajectory('wire3.traj')
    arm.playback_trajectory()
    arm.playback_trajectory(wait=True)

# ============================================
# AUTO-GENERATE BUTTONS
# ============================================

def create_buttons():
    import inspect

    # Get all functions defined in this module (excluding imported ones and built-ins)
    functions = []
    for name, obj in globals().items():
        if inspect.isfunction(obj) and obj.__module__ == "__main__":
            # Exclude these specific functions from becoming buttons
            if name not in ['create_buttons']:
                functions.append((name, obj))

    # Sort alphabetically for consistent ordering
    functions.sort(key=lambda x: x[0])

    # Create buttons for each function
    for i, (name, func) in enumerate(functions, 1):
        btn = tk.Button(button_frame,
                        text=name,
                        fg='black',
                        command=func,
                        width=20)
        btn.grid(column=0, row=i, padx=10, pady=5)


create_buttons()
window.mainloop()