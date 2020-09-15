import pandas as pd
from api.models import BikeParking
from django.contrib.gis.geos import Point
from django.utils.text import slugify


def get_capacity(text):
    if "(cp-7)" in text:
        return 7
    elif "(cp-3)" in text:
        return 3
    elif "(svtrgo8)" in text:
        return 8
    else:
        return 1

def run():
    url = "http://donnees.ville.montreal.qc.ca/dataset/c4dfdeb1-cdb7-44f4-8068-247755a56cc6/resource/78dd2f91-2e68-4b8b-bb4a-44c1ab5b79b6/download/supportvelosigs.csv"
    bike_parkings = pd.read_csv(url, encoding='latin-1')
    bike_parkings = bike_parkings.drop(['INV_NO', 'ANC_NUM', 'INV_CATL_NO', 'CATL_MODELE',
    'DATE_INSPECTION', 'CE_NO', 'ELEMENT', 'CATEGORIE', 'COULEUR', 'TERRITOIRE',
    'CONDITION', 'INTERVENTION', 'EMPL_Z', 'STATUT', 'BASE', 'ANCRAGE',
    'AIRE', 'ORDRE_AFFICHAGE', 'MATERIAU', 'EMPL_ID', 'EMPL_X', 'EMPL_Y'], axis=1)

    bike_parkings["PARC"] = bike_parkings["PARC"].fillna("Québec")

    bike_parkings['CAPACITY'] = bike_parkings["MARQ"].apply(get_capacity)
    bike_parkings['DESCRIPTION'] = bike_parkings["MARQ"] + " situé au " + bike_parkings["PARC"]
    bike_parkings["NAME"] = "Arceau no." + bike_parkings['INV_ID'].astype(str)
    bike_parkings["SLUG"] = bike_parkings['INV_ID'].apply(slugify)

    bike_parkings = bike_parkings.drop(['MARQ', 'PARC', 'INV_ID'], axis=1)

    print(bike_parkings.head())
    #print("____________________")
    #print(bike_parkings.count())
    print("____________________")
    print(bike_parkings.nunique())

    print(bike_parkings.isna().sum())

    for index, bike_parking in bike_parkings.iterrows():
        #print(bike_parking)
        position = Point(bike_parking['LONG'], bike_parking['LAT'])
        BikeParking.objects.update_or_create(slug=bike_parking['SLUG'],
                            defaults=dict(
                            name=bike_parking['NAME'],
                            description=bike_parking['DESCRIPTION'],
                            capacity= bike_parking['CAPACITY'],
                            position=position))
