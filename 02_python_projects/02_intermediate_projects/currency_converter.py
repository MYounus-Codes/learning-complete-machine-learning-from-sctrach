## Currency Converter
## This script converts one currency into another using live-style rate data.
## If no live API key is available, it uses sample exchange rates.

import os

import requests


def get_sample_rates() -> dict[str, float]:
    return {
        "USD": 1.0,
        "EUR": 0.92,
        "PKR": 278.0,
        "GBP": 0.79,
        "JPY": 156.0,
    }


def get_exchange_rates(base_currency: str = "USD") -> dict[str, float]:
    api_key = os.getenv("EXCHANGE_API_KEY")

    if not api_key:
        print("No API key found. Using sample exchange rates.")
        return get_sample_rates()

    url = f"https://api.exchangerate.host/latest?base={base_currency}&apikey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("rates", get_sample_rates())
    except requests.RequestException as exc:
        print(f"API request failed: {exc}")
        return get_sample_rates()


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    rates = get_exchange_rates(from_currency)
    from_rate = rates.get(from_currency, 1.0)
    to_rate = rates.get(to_currency, 1.0)
    return amount * (to_rate / from_rate)


if __name__ == "__main__":
    amount = float(input("Enter amount: ").strip() or 100)
    from_currency = input("From currency (USD, EUR, PKR, GBP, JPY): ").strip().upper() or "USD"
    to_currency = input("To currency (USD, EUR, PKR, GBP, JPY): ").strip().upper() or "PKR"

    converted = convert_currency(amount, from_currency, to_currency)
    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
