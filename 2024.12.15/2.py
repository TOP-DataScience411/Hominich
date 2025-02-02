from datetime import datetime, time, date
from decimal import Decimal
import numbers

class PowerMeter:
    def __init__(
        self,
        tariff1: numbers.Number = 6.5,
        tariff2: numbers.Number = 4.0,
        tariff2_starts: time = time(23, 0),
        tariff2_ends: time = time(6, 0),
    ):
        self.tariff1 = Decimal(tariff1).quantize(Decimal('0.01'))
        self.tariff2 = Decimal(tariff2).quantize(Decimal('0.01'))
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = Decimal('0.0')
        self.charges = {}

    def __repr__(self):
        return f"<PowerMeter: {self.power} kWh>"

    def __str__(self):
        if not self.charges:
            return print("Нет данных о начислениях")
        latest_month = max(self.charges)
        month_str = latest_month.strftime("(%b)")
        return f"{month_str} {self.charges[latest_month]}"

    def meter(self, power: numbers.Number) -> Decimal:
        if not isinstance(power, numbers.Number) or power <= 0:
            raise ValueError("Ошибка: потребление электроэнергии должно быть больше 0.")

        power = Decimal(power).quantize(Decimal('0.01'))
        self.power += power

        now = datetime.now()
        current_time = now.time()

        if self.tariff2_starts < self.tariff2_ends:
            is_tariff2 = self.tariff2_starts <= current_time < self.tariff2_ends
        else:
            is_tariff2 = current_time >= self.tariff2_starts or current_time < self.tariff2_ends

        rate = self.tariff2 if is_tariff2 else self.tariff1
        cost = (power * rate).quantize(Decimal('0.01'))

        month_key = date(now.year, now.month, 1)
        if month_key in self.charges:
            self.charges[month_key] += cost
        else:
            self.charges[month_key] = cost

        return cost

# python3 -i 2.py
# >>> pm1 = PowerMeter()
# >>> pm1.meter(2)
# Decimal('13.00')
# >>> pm1.meter(1.2)
# Decimal('7.80')
# >>> pm1
# <PowerMeter: 3.20 kWh>
# >>> print(pm1)
# (Jan) 20.80
# >>>
