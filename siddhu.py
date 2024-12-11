import tkinter as tk
from tkinter import ttk, messagebox

def currency_converter():
    rates = {
        "USD": 1.0,       # Base currency
        "INR": 82.5,      # 1 USD = 82.5 INR
        "EUR": 0.91,      # 1 USD = 0.91 EUR
        "GBP": 0.78,      # 1 USD = 0.78 GBP
        "ZAR": 17.85,    # 1 USD = 17.85 ZAR
        "JPY": 136.5,     # 1 USD = 136.5 JPY
        "RUB": 106.18,    # 1 USD = 106.18 RUB
        "AUD": 1.55,      # 1 USD = 1.55 AUD
        "CNY": 7.22,      # 1 USD = 7.22 CNY
    }

    def convert_currency():
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()
        amount_str = amount_entry.get()

        if from_currency not in rates or to_currency not in rates:
            messagebox.showerror("Error", "Invalid currency code selected.")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
            return

        converted_amount = (amount / rates[from_currency]) * rates[to_currency]
        result_label.config(
            text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
        )

    # Create the main window
    root = tk.Tk()
    root.title("Currency Converter")

    # Title label
    title_label = tk.Label(root, text="Simple Currency Converter", font=("Arial", 16))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # From currency
    from_currency_label = tk.Label(root, text="From Currency:")
    from_currency_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    from_currency_combobox = ttk.Combobox(root, values=list(rates.keys()), state="readonly")
    from_currency_combobox.grid(row=1, column=1, padx=10, pady=5)
    from_currency_combobox.set("USD")

    # To currency
    to_currency_label = tk.Label(root, text="To Currency:")
    to_currency_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    to_currency_combobox = ttk.Combobox(root, values=list(rates.keys()), state="readonly")
    to_currency_combobox.grid(row=2, column=1, padx=10, pady=5)
    to_currency_combobox.set("INR")

    # Amount
    amount_label = tk.Label(root, text="Amount:")
    amount_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=3, column=1, padx=10, pady=5)

    # Convert button
    convert_button = tk.Button(root, text="Convert", command=convert_currency)
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Result
    result_label = tk.Label(root, text="", font=("Arial", 14))
    result_label.grid(row=5, column=0, columnspan=2, pady=10)

    # Run the application
    root.mainloop()

if __name__ == "_main_":
    currency_converter()