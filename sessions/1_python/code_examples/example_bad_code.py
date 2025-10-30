# Script to process neuroimaging data for two subjects
# Requires numpy and nibabel
# pip install nibabel numpy

import numpy as n
import nibabel as ni

THR = 150
S_SIZE = 64

# =======================================================
#               PROCESSING FOR SUBJ_001
# =======================================================


dat1 = n.random.randint(0, 300, size=(S_SIZE, S_SIZE, S_SIZE), dtype=n.int16)
SCALAR_VAL = 2.0
hdr1 = n.array([[SCALAR_VAL, 0., 0., -100.],
                 [0., SCALAR_VAL, 0., -100.],
                 [0., 0., SCALAR_VAL, -100.],
                 [0., 0., 0., 1.  ]])
img1 = ni.Nifti1Image(dat1, hdr1)
print(f"Loaded image data for Subj 001 with shape: {dat1.shape}")

a = n.mean(dat1)
b = n.max(dat1)
c = n.min(dat1)

print(f"Subj 001 Stats: Mean={a:.2f}, Max={b}, Min={c}")

p_dat = n.copy(dat1)
p_dat[p_dat < THR] = 0
print(f"Applied threshold {THR} to Subj 001 data.")

out_dat_1 = ni.Nifti1Image(p_dat, hdr1)
ni.save(out_dat_1, 'test/results/s1_th_img.nii.gz')
print(f"Saved processed data for Subj 001.")


# =======================================================
#               PROCESSING FOR SUBJ_002
# =======================================================

S_SIZE = 128

dat2 = n.random.randint(0, 300, size=(S_SIZE, S_SIZE, S_SIZE), dtype=n.int16)
A_SCALAR = 2.0
hdr2 = n.array([[A_SCALAR, 0., 0., -100.],
                 [0., A_SCALAR, 0., -100.],
                 [0., 0., A_SCALAR, -100.],
                 [0., 0., 0., 1.  ]])
img2 = ni.Nifti1Image(dat2, hdr2)
print(f"Loaded image data for Subj 002 with shape: {dat2.shape}")

a2 = n.mean(dat2)
b2 = n.max(dat2)
c2 = n.min(dat2)

print(f"Subj 002 Stats: Mean={a2:.2f}, Max={b2}, Min={c2}")

p_dat2 = n.copy(dat2)
p_dat2[p_dat2 < THR] = 0
print(f"Applied threshold {THR} to Subj 002 data.")

out_dat_2 = ni.Nifti1Image(p_dat2, hdr2)
ni.save(out_dat_2, 'test/results/s1_th_img.nii.gz')
print(f"Saved processed data for Subj 002.")
