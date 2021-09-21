import numpy as np
import math
 
def rotationMatrixToEulerAngles(R):
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])
    singular = sy < 1e-6
    if not singular:
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else:
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
    return np.array([math.degrees(x), math.degrees(y), math.degrees(z)])


print(rotationMatrixToEulerAngles(np.array([
    [-0.99976446994532143393, -0.021713925739679539203, 0.000000008641004003622972278],
    [0.021668085842440610703, -0.99769595054491754805, -0.064290172235465801237],
    [0.0013959294167738118788, -0.064274857340369974641, 0.99793150511105667992]])))