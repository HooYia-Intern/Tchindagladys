import tkinter as tk
from tkinter import ttk, messagebox

class InvoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice System")
        self.root.geometry("600x600")

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Invoice System", font=("Helvetica", 16))
        title.pack(pady=10)

        # Customer Name
        tk.Label(self.root, text="Customer Name:").pack(pady=5)
        self.customer_name = tk.Entry(self.root, width=50)
        self.customer_name.pack(pady=5)

     
        # Item Entry
        tk.Label(self.root, text="Item Description:").pack(pady=5)
        self.item_description = tk.Entry(self.root, width=50)
        self.item_description.pack(pady=5)

        tk.Label(self.root, text="Quantity:").pack(pady=5)
        self.quantity = tk.Entry(self.root, width=20)
        self.quantity.pack(pady=5)

        
        tk.Label(self.root, text="Price:").pack(pady=5)
        self.price = tk.Entry(self.root, width=20)
        self.price.pack(pady=5)

        tk.Label(self.root, text="Tax (%):").pack(pady=5)
        self.tax = tk.Entry(self.root, width=20)
        self.tax.pack(pady=5)

        tk.Label(self.root, text="Discount (%):").pack(pady=5)
        self.discount = tk.Entry(self.root, width=20)
        self.discount.pack(pady=5)

        # Add Item Button
        self.add_item_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_item_button.pack(pady=10)

        # Items List
        self.items_list = ttk.Treeview(self.root, columns=("Description", "Quantity", "Price", "Tax", "Discount"))
        self.items_list.heading("#0", text="Item ID")
        self.items_list.heading("Description", text="Description")
        self.items_list.heading("Quantity", text="Quantity")
        self.items_list.heading("Price", text="Price")
        self.items_list.heading("Tax", text="Tax")
        self.items_list.heading("Discount", text="Discount")
        

        self.items_list.pack(pady=10)

        # Generate Invoice Button
        self.generate_invoice_button = tk.Button(self.root, text="Generate Invoice", command=self.generate_invoice)
        self.generate_invoice_button.pack(pady=10)

        # Invoice Text Area
        self.invoice_area = tk.Text(self.root, width=70, height=10)
        self.invoice_area.pack(pady=10)

        self.items = []
        self.item_id = 0

    def add_item(self):
        description = self.item_description.get()
        quantity = self.quantity.get()
        price = self.price.get()
        tax = self.tax.get()
        discount = self.discount.get()

        if (description and quantity.isdigit() and 
            price.replace('.', '', 1).isdigit() and 
            tax.replace('.', '', 1).isdigit() and 
            discount.replace('.', '', 1).isdigit()):
            
            self.item_id += 1
            self.items.append((self.item_id, description, int(quantity), 
                               float(price), float(tax), float(discount)))
            self.items_list.insert("", "end", iid=self.item_id, 
                                   text=self.item_id, 
                                   values=(description, quantity, price, tax, discount))


            self.item_description.delete(0, tk.END)
            self.quantity.delete(0, tk.END)
            self.price.delete(0, tk.END)
            self.tax.delete(0, tk.END)
            self.discount.delete(0, tk.END)
        else:
            messagebox.showerror("Input Error", "Please enter valid item details.")

    def generate_invoice(self):
        customer = self.customer_name.get()
        if not customer or not self.items:
            messagebox.showerror("Input Error", "Please enter customer name and add items.")
            return

        self.invoice_area.delete(1.0, tk.END)
        total = 0.0
        invoice_text = f"Invoice for {customer}\n\n"
        invoice_text += "Item ID | Description | Quantity | Price | Tax | Discount\n"
        invoice_text += "-" * 70 + "\n"

        for item in self.items:
            item_id, description, quantity, price, tax, discount = item
            total_price = quantity * price
            total_tax = total_price * (tax / 100)
            total_discount = total_price * (discount / 100)
            final_price = total_price + total_tax - total_discount
            
            total += final_price
            invoice_text += (f"{item_id:<8} | {description:<12} | {quantity:<8} | "
                             f"{price:.2f} | {tax:.2f} | {discount:.2f} | {final_price:.2f}\n")

        invoice_text += "-" * 70 + "\n"
        invoice_text += f"Total: {total:.2f}"

        self.invoice_area.insert(tk.END, invoice_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()