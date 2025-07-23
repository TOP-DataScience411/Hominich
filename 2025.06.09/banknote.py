import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Загрузка и подготовка данных
df = pd.read_csv("banknote-auth.csv")
X = df.drop(columns="class")
y = df["class"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Bagging
bagging_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=5),
    n_estimators=50,
    random_state=42,
    n_jobs=-1
)
bagging_model.fit(X_train, y_train)
y_pred_bag = bagging_model.predict(X_test)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Stacking
base_models = [
    ('dt', DecisionTreeClassifier(max_depth=5)),
    ('svc', SVC(probability=True))
]
stacking_model = StackingClassifier(
    estimators=base_models,
    final_estimator=LogisticRegression(),
    n_jobs=-1
)
stacking_model.fit(X_train, y_train)
y_pred_stack = stacking_model.predict(X_test)

# Оценка точности
accuracies = {
    "Bagging": accuracy_score(y_test, y_pred_bag),
    "Random Forest": accuracy_score(y_test, y_pred_rf),
    "Stacking": accuracy_score(y_test, y_pred_stack),
}

# Сравнение точности
plt.figure(figsize=(8, 5))
plt.bar(accuracies.keys(), accuracies.values(), color=['#FFC0CB', '#FFB6C1', '#FF69B4'])
plt.ylabel("Accuracy")
plt.title("Сравнение точности ансамблевых моделей")
plt.ylim(0.9, 1.0)
for i, acc in enumerate(accuracies.values()):
    plt.text(i, acc - 0.015, f"{acc:.3f}", ha='center', va='top', fontsize=12, color='#880E4F')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Матрицы ошибок
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
pink_cmap = plt.cm.Reds

for ax, model_name, y_pred in zip(
    axs,
    ["Bagging", "Random Forest", "Stacking"],
    [y_pred_bag, y_pred_rf, y_pred_stack]
):
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fake", "Real"])
    disp.plot(ax=ax, cmap=pink_cmap, colorbar=False, values_format='d')
    ax.set_title(f"Матрица ошибок: {model_name}")

plt.tight_layout()
plt.show()
