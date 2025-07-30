import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sys import path

# Загрузка данных
data_path = Path(path[0]) / "data1.npz"
data = np.load(data_path)

x = data['x']
y = data['y']

# Визуализация исходных данных
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='gray', alpha=0.7, label='Исходные данные')
plt.title("Исходные данные")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("Исходные данные.png", dpi=300)
plt.show()

X = x.reshape(-1, 1)

# Обучение модели RANSAC
ransac = RANSACRegressor(estimator=LinearRegression(),
                         min_samples=2,
                         residual_threshold=0.35,
                         random_state=42)
ransac.fit(X, y)
y_pred = ransac.predict(X)

inlier_mask = ransac.inlier_mask_
outlier_mask = ~inlier_mask

# Визуализация RANSAC
plt.figure(figsize=(10, 6))
plt.scatter(x[inlier_mask], y[inlier_mask], color='cyan', label='Линейный кластер')
plt.scatter(x[outlier_mask], y[outlier_mask], color='pink', label='Другое')
plt.plot(x, y_pred, color='black', label='RANSAC Regression', linewidth=2)
plt.title("RANSAC-регрессия на исходных данных")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("RANSAC-регрессия на исходных данных.png", dpi=300)
plt.show()

# Выделяем линейную часть
inliers = np.column_stack((x[inlier_mask], y[inlier_mask]))
