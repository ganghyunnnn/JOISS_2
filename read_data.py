import pandas as pd
import math

f_topo = '2002-2004_topo.csv'
f_station = '2002-2004_station.csv'

f_u1a = '2002-2004_U1a.csv'
f_u1b = '2002-2004_U1b.csv'
f_u2a = '2002-2004_U2a.csv'
f_u2b = '2002-2004_U2b.csv'
f_u3a = '2002-2004_U3a.csv'
f_u3b = '2002-2004_U3b.csv'
f_list = [f_u1a, f_u1b, f_u2a, f_u2b, f_u3a, f_u3b]

topo = pd.read_csv(f_topo, encoding='cp949')
station = pd.read_csv(f_station, encoding='cp949')

sta_lon = list(station.iloc[:, 1])
sta_lat = list(station.iloc[:, 2])

sta_width, sta_thickness = [], []
for i in range(0, 3):
    sta_width.append(sta_lon[i+1] - sta_lon[i])
    sta_thickness.append(abs(sta_lat[+1] - sta_lat[i]))

width = []
for j, k in zip(sta_width, sta_lat):
    width.append((2 * math.pi * 6400 * math.cos(k) / 360) * j) # 경도 1도(km) = 2 x 파이 x 지구 반지름 x cos(위도) / 360

# thickness = []
# for l in sta_thickness:
#     thickness.append(48000 / 360 * l)

zero = 1500
height = [(2090-zero)*0.001, (2250-zero)*0.001, (2235-zero)*0.001] # 높이

area = []
for l, m in zip(width, height):
    area.append(l * m) # 면적

sv_1a, sv_1b, sv_2a, sv_2b, sv_3a, sv_3b = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
sv_1a = area[0] * pd.read_csv(f_list[0]).iloc[:, -1]
sv_1b = area[0] * pd.read_csv(f_list[1]).iloc[:, -1]
sv_2a = area[1] * pd.read_csv(f_list[2]).iloc[:, -1]
sv_2b = area[1] * pd.read_csv(f_list[3]).iloc[:, -1]
sv_3a = area[2] * pd.read_csv(f_list[4]).iloc[:, -1]
sv_3b = area[2] * pd.read_csv(f_list[5]).iloc[:, -1]

sv_1a.to_csv('sv_1a.csv', index=False)
sv_1b.to_csv('sv_1b.csv', index=False)
sv_2a.to_csv('sv_2a.csv', index=False)
sv_2b.to_csv('sv_2b.csv', index=False)
sv_3a.to_csv('sv_3a.csv', index=False)
sv_3b.to_csv('sv_3b.csv', index=False)
