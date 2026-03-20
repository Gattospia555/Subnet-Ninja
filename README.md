# 🥷 Subnet-Ninja CLI

Un calcolatore di subnet a riga di comando elegante, veloce e colorato, sviluppato in Python. 

Creato come strumento pratico, questo script permette di calcolare rapidamente i parametri fondamentali di una rete IPv4 direttamente dal terminale.

## ✨ Funzionalità

* **Calcolo istantaneo:** Restituisce Indirizzo di Rete, Subnet Mask, Indirizzo di Broadcast, Range di Host utilizzabili e Numero Totale di Host.
* **Supporto CIDR:** Accetta in input notazioni standard come `192.168.1.0/24` o anche indirizzi host come `10.0.0.5/8` per calcolarne la rete di appartenenza.
* **Design curato:** Output formattato in tabelle leggibili e colorate grazie alla libreria `rich`.
* **CLI nativa:** Utilizza `argparse` per un'esperienza da terminale fluida e professionale, con menu di aiuto integrato.

## 🛠️ Prerequisiti

* Python 3.x installato sul sistema.
* Libreria Python `rich`.

## 🚀 Installazione

1. Clona questo repository in locale:
   ```bash
   git clone https://github.com/TUO-USERNAME/subnet-ninja.git
   cd subnet-ninja
   ```

2. Installa la dipendenza necessaria:
   ```bash
   pip install rich
   ```

## 💻 Utilizzo
Esegui lo script passando l'indirizzo IP e la subnet mask (in formato CIDR) come argomento.

Esempio di base:

```bash
python subnet_ninja.py 192.168.1.0/24
```

Per visualizzare il manuale di aiuto integrato:

```bash
python subnet_ninja.py -h
```
