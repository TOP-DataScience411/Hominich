import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
from task1_1 import x, y, inliers

inliers = np.array(inliers)
x_inliers = inliers[:, 0].reshape(-1, 1)
y_inliers = inliers[:, 1]

# 1. Модель на всей выборке
x_full = x.reshape(-1, 1)
y_full = y

x_train_full, x_test_full, y_train_full, y_test_full = train_test_split(
    x_full, y_full, test_size=0.2, random_state=1
)

model_full = LinearRegression()
model_full.fit(x_train_full, y_train_full)
y_pred_full = model_full.predict(x_test_full)

r2_full = r2_score(y_test_full, y_pred_full)
rmse_full = root_mean_squared_error(y_test_full, y_pred_full)

# 2. Модель на inliers
x_train_in, x_test_in, y_train_in, y_test_in = train_test_split(
    x_inliers, y_inliers, test_size=0.2, random_state=1
)

model_in = LinearRegression()
model_in.fit(x_train_in, y_train_in)
y_pred_in = model_in.predict(x_test_in)

r2_in = r2_score(y_test_in, y_pred_in)
rmse_in = root_mean_squared_error(y_test_in, y_pred_in)

# 3. Визуализация
x_line = np.linspace(x.min(), x.max(), 500).reshape(-1, 1)
y_line_full = model_full.predict(x_line)
y_line_in = model_in.predict(x_line)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='lightgray', label='Исходные данные')
plt.plot(x_line, y_line_full, color='green', linewidth=2, label=f'Вся выборка (R²={r2_full:.3f})')
plt.plot(x_line, y_line_in, color='blue', linestyle='--', linewidth=2, label=f'Inliers (R²={r2_in:.3f})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Сравнение моделей линейной регрессии')
plt.legend()
plt.grid(True)
plt.savefig("Линейная регрессия.png", dpi=300, bbox_inches='tight')
plt.show()

# Вывод результатов
print("--- Регрессия на всей выборке ---")
print(f"R² = {r2_full:.3f}")
print(f"RMSE = {rmse_full:.3f}")

print("\n--- Регрессия на inliers ---")
print(f"R² = {r2_in:.3f}")
print(f"RMSE = {rmse_in:.3f}")
