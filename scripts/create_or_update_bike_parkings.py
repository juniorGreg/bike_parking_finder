import pandas as pd
from api.models import BikeParking

def run():
    url = "http://donnees.ville.montreal.qc.ca/dataset/c4dfdeb1-cdb7-44f4-8068-247755a56cc6/resource/78dd2f91-2e68-4b8b-bb4a-44c1ab5b79b6/download/supportvelosigs.csv"
    bike_parkings = pd.read_csv(url, encoding='latin-1')

    print(bike_parkings.head())
    print("____________________")
    print(bike_parkings.count())
    print("____________________")
    print(bike_parkings.nunique())
