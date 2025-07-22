import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Загрузка и очистка
df_oil_raw = pd.read_csv("urals_oil_rus_export_prices.csv")
df_diesel_raw = pd.read_csv("dizel_fuel_rus_prices.csv")

russian_months = {
    'янв': 'Jan', 'фев': 'Feb', 'мар': 'Mar', 'апр': 'Apr', 'май': 'May',
    'июн': 'Jun', 'июл': 'Jul', 'авг': 'Aug', 'сен': 'Sep', 'окт': 'Oct',
    'ноя': 'Nov', 'дек': 'Dec'
}

def parse_russian_date_price(row_str):
    parts = str(row_str).split()
    if len(parts) != 2:
        return None, None
    date_str, price_str = parts
    for ru, en in russian_months.items():
        if ru in date_str:
            date_str = date_str.replace(ru, en)
            break
    try:
        date = datetime.strptime(date_str, "%d.%b.%y")
        price = float(price_str.replace(',', '.'))
        return date, price
    except:
        return None, None

def clean_dataframe(df_raw):
    dates, prices = [], []
    for value in df_raw.iloc[:, 0]:
        d, p = parse_russian_date_price(value)
        if d and p:
            dates.append(d)
            prices.append(p)
    return pd.DataFrame({'date': dates, 'price': prices}).sort_values('date')

df_oil = clean_dataframe(df_oil_raw)
df_diesel = clean_dataframe(df_diesel_raw)

# Подготовка данных
dates_oil = df_oil['date'].tolist()
dates_diesel = df_diesel['date'].tolist()
prices_oil = df_oil['price'].to_numpy()
prices_diesel = df_diesel['price'].to_numpy()

# Корреляция со сдвигом
def shift_and_correlate(months_shift):
    shifted_dates = np.array([d + relativedelta(months=months_shift) for d in dates_oil])
    df_shifted = pd.DataFrame({'date': shifted_dates, 'price_oil': prices_oil})
    df_diesel_local = pd.DataFrame({'date': dates_diesel, 'price_diesel': prices_diesel})
    df_merged = pd.merge(df_shifted, df_diesel_local, on='date', how='inner')
    if len(df_merged) < 2:
        return None, None, None
    x = df_merged['price_oil'].to_numpy()
    y = df_merged['price_diesel'].to_numpy()
    corr = np.corrcoef(x, y)[0, 1]
    return x, y, corr

# Поиск лучшего сдвига
best_corr = -np.inf
best_shift = None
best_x = best_y = None

print("Сдвиг | Корреляция | X (нефть) → | Y (дизель) →")
print("-" * 80)

for shift in range(-12, 13):
    x, y, corr = shift_and_correlate(shift)
    if x is None: continue
    print(f"{shift:+4}  | {corr:+.4f}   | {np.round(x, 1)} | {np.round(y, 2)}")
    if corr > best_corr:
        best_corr = corr
        best_shift = shift
        best_x = x
        best_y = y

# Линейная регрессия
a, b = np.polyfit(best_x, best_y, 1)
regression_eq = f"y = {a:.4f} * x + {b:.4f}"

print("\n=== ЛУЧШИЙ РЕЗУЛЬТАТ ===")
print(f"Сдвиг: {best_shift} месяцев")
print(f"Коэффициент корреляции: {best_corr:.4f}")
print("Уравнение регрессии:", regression_eq)

# График
plt.figure(figsize=(10, 6))
plt.scatter(best_x, best_y, label='Наблюдения', color='blue')
plt.plot(best_x, a * best_x + b, color='red', label='Линия регрессии')
plt.title(f'Линейная регрессия (сдвиг {best_shift} мес, r = {best_corr:.4f})')
plt.xlabel('Цена нефти')
plt.ylabel('Цена дизеля')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("regression_result.png", dpi=300)
plt.show()

# Сдвиг | Корреляция | X (нефть) → | Y (дизель) →
# --------------------------------------------------------------------------------
#  -12  | +0.6355   | [270.2 327.6 354.9 483.7 456.6 535.8 448.5] | [34.34 34.6  35.25 37.6  37.66 39.   44.47]
#  -11  | +0.6115   | [243.7 341.4 351.9 485.5 483.7 592.1 462.1] | [34.34 34.6  35.25 37.6  37.66 39.   44.47]
#  -10  | +0.3846   | [207.2 305.1 365.3 456.5 485.5 543.5 486.6 345.1] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -9  | +0.6494   | [237.  270.2 381.5 435.2 456.5 518.7 527.3 419.7] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -8  | +0.7403   | [287.7 243.7 388.7 405.6 435.2 536.8 503.9 477.6] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -7  | +0.6783   | [323.6 207.2 383.5 378.3 405.6 549.1 475.  471.2] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -6  | +0.6747   | [344.4 237.  349.1 365.5 378.3 524.7 450.4 447.7] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -5  | +0.7211   | [330.9 287.7 328.4 333.3 365.5 480.3 408.4 438.6] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -4  | +0.7560   | [373.  323.6 333.8 354.9 333.3 456.6 441.4 434.5] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -3  | +0.6854   | [430.1 344.4 332.  351.9 354.9 483.7 535.8 448.5] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99]
#   -2  | +0.3734   | [453.8 330.9 303.5 365.3 351.9 485.5 592.1 462.1 345.1] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04]
#   -1  | +0.5723   | [456.9 373.  327.6 381.5 365.3 456.5 543.5 486.6 419.7] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04]
#   +0  | +0.8322   | [390.4 430.1 341.4 388.7 381.5 435.2 518.7 527.3 477.6] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04]
#   +1  | +0.3810   | [424.5 453.8 305.1 383.5 388.7 405.6 536.8 503.9 471.2 345.1] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84]
#   +2  | +0.5943   | [364.9 456.9 270.2 349.1 383.5 378.3 549.1 475.  447.7 419.7] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84]
#   +3  | +0.7493   | [381.8 390.4 243.7 328.4 349.1 365.5 524.7 450.4 438.6 477.6] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84]
#   +4  | +0.2819   | [518.3 424.5 207.2 333.8 328.4 333.3 480.3 408.4 434.5 471.2 345.1] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#   +5  | +0.2858   | [603.5 364.9 237.  332.  333.8 354.9 456.6 441.4 448.5 447.7 419.7] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#   +6  | +0.2733   | [669.8 381.8 287.7 303.5 332.  351.9 483.7 535.8 462.1 438.6 477.6] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#   +7  | +0.0977   | [717.4 518.3 323.6 327.6 303.5 365.3 485.5 592.1 486.6 434.5 471.2] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#   +8  | -0.0711   | [756.2 603.5 344.4 341.4 327.6 381.5 456.5 543.5 527.3 448.5 447.7] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#   +9  | -0.1634   | [791.4 669.8 330.9 305.1 341.4 388.7 435.2 518.7 503.9 462.1 438.6] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#  +10  | -0.1879   | [785.9 717.4 373.  270.2 305.1 383.5 405.6 536.8 475.  486.6 434.5] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#  +11  | -0.1843   | [785.6 756.2 430.1 243.7 270.2 349.1 378.3 549.1 450.4 527.3 448.5] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#  +12  | -0.2200   | [770.5 791.4 453.8 207.2 243.7 328.4 365.5 524.7 408.4 503.9 462.1] | [34.34 34.6  35.25 37.6  37.66 39.   44.47 45.99 48.04 47.84 48.02]
#
# === ЛУЧШИЙ РЕЗУЛЬТАТ ===
# Сдвиг: 0 месяцев
# Коэффициент корреляции: 0.8322
# Уравнение регрессии: y = 0.0672 * x + 10.6137
#
