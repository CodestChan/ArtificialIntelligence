import matplotlib.pyplot as plt
import numpy as np
import cv2

img=cv2.imread('bathroom.jpg')
img_resize=cv2.resize(img,(768,480))
gaus=cv2.GaussianBlur(img_resize,(5,5),0)

gray = cv2.cvtColor(gaus, cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,100,200)

height, width = canny.shape
diag_len = int(np.ceil(np.sqrt(height ** 2 + width ** 2)))
accumulator = np.zeros((2 * diag_len, 180), dtype=np.uint8)

coords = np.argwhere(canny > 0)

for x, y in coords:
    for t in range(-90, 90):
        r = int((x * np.cos(np.deg2rad(t))) + (y * np.sin(np.deg2rad(t))))
        accumulator[r + diag_len, t + 90] += 1

lines = []
for r, theta in np.argwhere(accumulator >= 150):
    lines.append((r - diag_len, theta - 90))

for r, theta in lines:
    a = np.cos(np.deg2rad(theta))
    b = np.sin(np.deg2rad(theta))
    x0 = a * r
    y0 = b * r
    x1 = int(x0 + diag_len * (-b))
    y1 = int(y0 + diag_len * (a))
    x2 = int(x0 - diag_len * (-b))
    y2 = int(y0 - diag_len * (a))
    cv2.line(img_resize, (x1, y1), (x2, y2), (0, 0, 255), 2)


cv2.imshow('Hough',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

#绘制霍夫空间
# theta_range = np.deg2rad(np.arange(-90.0, 90.0))
# rho_range = np.arange(-diag_len, diag_len)
#
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.set_theta_zero_location('N')
# theta, rho = np.meshgrid(theta_range, rho_range)
# ax.contourf(theta, rho, accumulator, cmap='gray')
#
# plt.show()

# result=cv2.hconcat([gray,canny])
# cv2.imshow('Original and Canny',result)

#实验性代码
'''
theto=np.linspace(-90,90,200)
theto_f=np.deg2rad(theto)
coords = np.argwhere(canny > 0)

for x,y in coords:
    rho=x*np.cos(theto_f)+y*np.sin(theto_f)
    plt.plot(theto_f,rho)

plt.show()
r,c=canny.shape
x_ticks = np.arange(0, c+1, 1)
y_ticks = np.arange(0, r+1, 1)

b=np.argwhere(canny>0)
fig, ax = plt.subplots()
ax.scatter(b[:,0],b[:,1])
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.grid(True)
plt.show()
'''

#霍夫变换函数
'''
def hough_trans(image,threshold:int):
    height, width = image.shape
    diag_len = int(np.ceil(np.sqrt(height**2 + width**2)))
    accumulator = np.zeros((2 * diag_len, 180), dtype=np.uint8)

    coords=np.argwhere(image>0)

    for x, y in coords:
        for t in range(-90,90):
            r = int((x * np.cos(np.deg2rad(t))) + (y * np.sin(np.deg2rad(t))))
            accumulator[r + diag_len, t+90] += 1

    lines = []
    for r, theta in np.argwhere(accumulator >= threshold):
        lines.append((r - diag_len, theta-90))

    return lines
'''