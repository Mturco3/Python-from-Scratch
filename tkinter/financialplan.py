import tkinter as tk
from tkinter import messagebox

class PianoFinanziario:
    def __init__(self, root):
        self.root = root
        self.root.title("Piano Finanziario")

        # Dati finanziari
        self.entrate = []
        self.uscite = []

        # Frame per Entrate
        self.frame_entrate = tk.LabelFrame(self.root, text="Entrate")
        self.frame_entrate.pack(fill="both", expand="yes", padx=10, pady=5)

        self.lbl_entrata = tk.Label(self.frame_entrate, text="Descrizione:")
        self.lbl_entrata.grid(row=0, column=0, padx=5, pady=5)
        self.entrata_descrizione = tk.Entry(self.frame_entrate)
        self.entrata_descrizione.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_quantita_entrata = tk.Label(self.frame_entrate, text="Quantità:")
        self.lbl_quantita_entrata.grid(row=1, column=0, padx=5, pady=5)
        self.quantita_entrata = tk.Entry(self.frame_entrate)
        self.quantita_entrata.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_prezzo_entrata = tk.Label(self.frame_entrate, text="Prezzo per unità:")
        self.lbl_prezzo_entrata.grid(row=2, column=0, padx=5, pady=5)
        self.prezzo_entrata = tk.Entry(self.frame_entrate)
        self.prezzo_entrata.grid(row=2, column=1, padx=5, pady=5)

        self.btn_aggiungi_entrata = tk.Button(self.frame_entrate, text="Aggiungi Entrata", command=self.aggiungi_entrata)
        self.btn_aggiungi_entrata.grid(row=3, column=0, columnspan=2, pady=10)

        # Listbox per visualizzare le entrate
        self.listbox_entrate = tk.Listbox(self.frame_entrate, height=10, width=50)
        self.listbox_entrate.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Frame per Uscite
        self.frame_uscite = tk.LabelFrame(self.root, text="Uscite")
        self.frame_uscite.pack(fill="both", expand="yes", padx=10, pady=5)

        self.lbl_uscita = tk.Label(self.frame_uscite, text="Descrizione:")
        self.lbl_uscita.grid(row=0, column=0, padx=5, pady=5)
        self.uscita_descrizione = tk.Entry(self.frame_uscite)
        self.uscita_descrizione.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_quantita_uscita = tk.Label(self.frame_uscite, text="Quantità:")
        self.lbl_quantita_uscita.grid(row=1, column=0, padx=5, pady=5)
        self.quantita_uscita = tk.Entry(self.frame_uscite)
        self.quantita_uscita.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_prezzo_uscita = tk.Label(self.frame_uscite, text="Prezzo per unità:")
        self.lbl_prezzo_uscita.grid(row=2, column=0, padx=5, pady=5)
        self.prezzo_uscita = tk.Entry(self.frame_uscite)
        self.prezzo_uscita.grid(row=2, column=1, padx=5, pady=5)

        self.btn_aggiungi_uscita = tk.Button(self.frame_uscite, text="Aggiungi Uscita", command=self.aggiungi_uscita)
        self.btn_aggiungi_uscita.grid(row=3, column=0, columnspan=2, pady=10)

        # Listbox per visualizzare le uscite
        self.listbox_uscite = tk.Listbox(self.frame_uscite, height=10, width=50)
        self.listbox_uscite.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Frame per il Totale
        self.frame_totale = tk.Frame(self.root)
        self.frame_totale.pack(fill="both", expand="yes", padx=10, pady=5)

        self.btn_calcola_totale = tk.Button(self.frame_totale, text="Calcola Totale", command=self.calcola_totale)
        self.btn_calcola_totale.pack(side="left", padx=5)

        self.lbl_totale = tk.Label(self.frame_totale, text="Totale: 0")
        self.lbl_totale.pack(side="right", padx=5)

    def aggiungi_entrata(self):
        descrizione = self.entrata_descrizione.get()
        quantita = self.quantita_entrata.get()
        prezzo = self.prezzo_entrata.get()

        if descrizione and quantita.isdigit() and prezzo.isdigit():
            totale = int(quantita) * int(prezzo)
            self.entrate.append(totale)
            self.listbox_entrate.insert(tk.END, f"{descrizione}: {quantita} * {prezzo} = {totale}")
            messagebox.showinfo("Entrata Aggiunta", f"Entrata {descrizione} aggiunta con successo!")
            self.entrata_descrizione.delete(0, tk.END)
            self.quantita_entrata.delete(0, tk.END)
            self.prezzo_entrata.delete(0, tk.END)
        else:
            messagebox.showerror("Errore", "Per favore inserisci valori validi.")

    def aggiungi_uscita(self):
        descrizione = self.uscita_descrizione.get()
        quantita = self.quantita_uscita.get()
        prezzo = self.prezzo_uscita.get()

        if descrizione and quantita.isdigit() and prezzo.isdigit():
            totale = int(quantita) * int(prezzo)
            self.uscite.append(totale)
            self.listbox_uscite.insert(tk.END, f"{descrizione}: {quantita} * {prezzo} = {totale}")
            messagebox.showinfo("Uscita Aggiunta", f"Uscita {descrizione} aggiunta con successo!")
            self.uscita_descrizione.delete(0, tk.END)
            self.quantita_uscita.delete(0, tk.END)
            self.prezzo_uscita.delete(0, tk.END)
        else:
            messagebox.showerror("Errore", "Per favore inserisci valori validi.")

    def calcola_totale(self):
        totale_entrate = sum(self.entrate)
        totale_uscite = sum(self.uscite)
        totale = totale_entrate - totale_uscite
        self.lbl_totale.config(text=f"Totale: {totale}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PianoFinanziario(root)
    root.mainloop()
