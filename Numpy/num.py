import numpy as np
# Create arrays of zeros, ones, and an identity matrix
ar_0=np.zeros((2,3), dtype=int)
print(ar_0)
ar_1=np.ones((3,2), dtype=int)
ar_iden=np.eye(4)
print(ar_1)
print(ar_iden)
print(ar_0.shape)