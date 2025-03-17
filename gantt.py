import pandas as pd
import plotly.express as px

# Veriyi yükle ve düzenle
df = pd.read_excel("7 ürün.xlsx")
df[['Başlangıç', 'Bitiş']] = df['Saat Aralığı'].str.split(' - ', expand=True)
df['Başlangıç Tarih'] = pd.to_datetime(df['Tarih'] + ' ' + df['Başlangıç'])
df['Bitiş Tarih'] = pd.to_datetime(df['Tarih'] + ' ' + df['Bitiş'])

# Gantt şeması
fig = px.timeline(
    df,
    x_start="Başlangıç Tarih",
    x_end="Bitiş Tarih",
    y="Ürün",
    color="Operasyon",
    hover_name="Çalışanlar",
    title="Ürün Bazında İşçi Atamaları"
)
fig.update_yaxes(categoryorder="category ascending")
fig.show()