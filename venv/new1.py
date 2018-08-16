dc={
    "Meta Data": {
        "1. Information": "Weekly Prices and Volumes for Digital Currency",
        "2. Digital Currency Code": "BTC",
        "3. Digital Currency Name": "Bitcoin",
        "4. Market Code": "USD",
        "5. Market Name": "United States Dollar",
        "6. Last Refreshed": "2018-08-10 (end of day)",
        "7. Time Zone": "UTC"
    },
    "Time Series (Digital Currency Weekly)": {
        "2018-08-10": {
            "1a. open (USD)": "7052.73104063",
            "1b. open (USD)": "7052.73104063",
            "2a. high (USD)": "7151.91141695",
            "2b. high (USD)": "7151.91141695",
            "3a. low (USD)": "6071.41450474",
            "3b. low (USD)": "6071.41450474",
            "4a. close (USD)": "6165.02886932",
            "4b. close (USD)": "6165.02886932",
            "5. volume": "563695.38171400",
            "6. market cap (USD)": "3650959202.57999992"
        },
"2018-08-05": {
            "1a. open (USD)": "8214.98601708",
            "1b. open (USD)": "8214.98601708",
            "2a. high (USD)": "8241.23480669",
            "2b. high (USD)": "8241.23480669",
            "3a. low (USD)": "6921.93523864",
            "3b. low (USD)": "6921.93523864",
            "4a. close (USD)": "7044.08904097",
            "4b. close (USD)": "7044.08904097",
            "5. volume": "634372.97810200",
            "6. market cap (USD)": "4779791810.14000034"
        },
        "2018-07-29": {
            "1a. open (USD)": "7422.47706776",
            "1b. open (USD)": "7422.47706776",
            "2a. high (USD)": "8456.56225937",
            "2b. high (USD)": "8456.56225937",
            "3a. low (USD)": "7408.49267459",
            "3b. low (USD)": "7408.49267459",
            "4a. close (USD)": "8211.75844822",
            "4b. close (USD)": "8211.75844822",
            "5. volume": "659483.98964900",
            "6. market cap (USD)": "5355123659.93000031"
        }
    }
    }
import pandas as pd
dc2 = dc['Time Series (Digital Currency Weekly)']
for k in dc2.keys():
    print(k)
df = pd.DataFrame(dc['Time Series (Digital Currency Weekly)'])
print(df)
print("done")
self.snap = tk.PhotoImage(file="fb_logo.png")
        self.snap = self.snap.subsample(10,10)
        self.lbl = tk.Label(self, image=self.snap)
        self.lbl.pack(pady=10, padx=10)