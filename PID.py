import time

import matplotlib
import matplotlib.pyplot as pl

init_value = 0.0
setpoint = 4.0

kp = 0.5
ki = 0.01
kd = 0.8

max_effort = 1.0
min_effort = 0.0

t = 0
tmax = 100
step = 1


values = []
times = []

def err(value, setpoint):
    return setpoint - value

def int(value, step, tot_err):
    tot_err = tot_err + err(value, setpoint)*step
    return tot_err

def diff(value, step, prev_err):
    return (err(value, setpoint) - prev_err)/step

def PID(init_value, setpoint, kp, ki, kd, max_effort, min_effort, t, tmax, step, tot_err, prev_err):
    value = init_value
    while(t<tmax):
        prev_err = err(value, setpoint)
        tot_err = int(value, step, tot_err)
        value = value + kp*err(value, setpoint) + ki*tot_err + kd*diff(value, step, prev_err)
        print(value)
        values.append(value)
        times.append(t)
        t += 1
        time.sleep(0.05)

PID(init_value, setpoint, kp, ki, kd, max_effort, min_effort, t, tmax, step, 0, 0)

pl.plot(times, values)
pl.show()
