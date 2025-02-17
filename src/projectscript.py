#!/usr/bin/env python
# coding: utf-8
# %%
def get_minute_data():
    '''process minute data'''
    import numpy as np
    import datetime as dt

    tp_craig = np.loadtxt("./Data/Craigflower_Tp.dat")
    tp_cumb = np.loadtxt("./Data/Cumberland_Tp.dat")
    tp_mont = np.loadtxt("./Data/Monterey_Tp.dat")
    tp_shawn = np.loadtxt("./Data/ShawniganLake_Tp.dat")
    tp_uvic = np.loadtxt("./Data/UVicSci_Tp.dat")

    tp_all = [tp_craig,tp_cumb,tp_mont,tp_shawn,tp_uvic]
    temps = np.array([tp.T[0][2:] for tp in tp_all])
    press = np.array([tp.T[1][2:] for tp in tp_all])

    stations = ['Craigflower','Cumberland','Monterey','Shawnigan Lake','UVicSci']
    tt_start = dt.datetime(2016,1,1)
    N_pts = int(tp_craig[1,0])
    tt_mins = [tt_start + dt.timedelta(days = delta_t) for delta_t in np.linspace(0,tp_craig[0,1]- 
                                                                            tp_craig[0,0],N_pts)]

    return [temps,press,tt_mins,stations]

def get_hour_data():
    
    import numpy as np
    import datetime as dt
    
    press_all = np.loadtxt("./Data/UVic_weatherdata_pressure_hourly.dat")
    temp_all = np.loadtxt("./Data/UVic_weatherdata_temperature_hourly.dat")
    coast = np.loadtxt('./Data/VI_coast_updated.dat')
    
    locs = press_all[0:2].T[1:]
    press = press_all[3:].T[1:].T
    temps = temp_all[3:].T[1:].T
    tt = press_all.T[0][3:]
    
    tt = np.array([dt.datetime(2016,1,1) + dt.timedelta(days = ti) for ti in tt])

    return [tt,temps,press,locs,coast]




