from playwright.sync_api import sync_playwright

def main():
    list = ['Taman Desa', 'Sri Petaling', 'Setapak', 'Old Klang Road',
       'Kepong', 'Cheras', 'Desa Petaling', 'KLCC', 'Taman Melawati',
       'Bukit Jalil', 'Setiawangsa', 'KL City', 'Sungai Besi', 'Ampang',
       'Brickfields', 'Taman Permata', 'Bangsar South', 'Solaris Dutamas',
       'Pandan Indah', 'Mont Kiara', 'Others', 'Wangsa Maju',
       'City Centre', 'Sentul', 'Jalan Ipoh', 'Gombak', 'Titiwangsa',
       'Jalan Kuching', 'Pandan Perdana', 'Sri Damansara', 'Segambut',
       'Bukit Tunku', 'Pantai', 'OUG', 'Desa Pandan', 'Pandan Jaya',
       'Taman Tun Dr Ismail', 'KL Sentral', 'Keramat',
       'Bandar Damai Perdana', 'Bukit Bintang', 'Damansara',
       'Bandar Tasik Selatan', 'Taman Duta', 'Chan Sow Lin', 'Pudu',
       'Kuchai Lama', 'Seputeh', 'Bangsar', 'Sri Hartamas',
       'Mid Valley City', 'Ampang Hilir', 'Damansara Heights',
       'Desa ParkCity', 'Jinjang', 'Jalan Sultan Ismail',
       'Bukit Persekutuan', 'Puchong', 'Bandar Menjalara', 'Pekan Batu',
       'Salak Selatan', 'Sungai Penchala', 'KL Eco City', 'Batu',
       'Serdang', 'Bukit Ledang', 'Country Heights Damansara',
       'Country Heights', 'Setia Eco Park']
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False, slow_mo = 1000)
        page = browser.new_page()
        page.set_default_timeout(3000)
        for i in list:
            try:
                page.goto(f'https://www.google.com/search?q={i}+coordinates')
                coords = page.locator('div[data-attrid="kc:/location/location:coordinates"]').nth(0)
                print(f"'{i}': [{coords.inner_text()}], ")
            except:
                print(f"'{i}': [None]")

if __name__ == '__main__':
    main()

"""
Results (For those regions where coordinates were unavailable, those are manually searched)
'Taman Desa': [3.1030° N, 101.6845° E], 
'Sri Petaling': [3.0684° N, 101.6856° E], 
'Setapak': [3.2791° N, 101.7410° E], 
'Old Klang Road': [None]
'Kepong': [3.2140° N, 101.6356° E], 
'Cheras': [3.1068° N, 101.7259° E], 
'Desa Petaling': [3.0835° N, 101.7105° E], 
'KLCC': [3.1466° N, 101.6958° E], 
'Taman Melawati': [3.2126° N, 101.7471° E], 
'Bukit Jalil': [3.0587° N, 101.6917° E], 
'Setiawangsa': [3.1830° N, 101.7462° E], 
'KL City': [3.1499° N, 101.6945° E], 
'Sungai Besi': [3.0574° N, 101.7179° E], 
'Ampang': [3.1491° N, 101.7625° E], 
'Brickfields': [3.1292° N, 101.6861° E], 
'Taman Permata': [3.2067° N, 101.7521° E], 
'Bangsar South': [3.1106° N, 101.6663° E], 
'Solaris Dutamas': [3.1709° N, 101.6661° E], 
'Pandan Indah': [3.1339° N, 101.7517° E], 
'Mont Kiara': [3.1685° N, 101.6512° E], 
'Others': [None]
'Wangsa Maju': [3.2038° N, 101.7367° E], 
'City Centre': [3.1466° N, 101.6958° E], 
'Sentul': [3.2066° N, 101.6820° E], 
'Jalan Ipoh': [3.1752° N, 101.6866° E], 
'Gombak': [3.2535° N, 101.6533° E], 
'Titiwangsa': [3.1774° N, 101.7077° E], 
'Jalan Kuching': [None]
'Pandan Perdana': [3.1172° N, 101.7421° E], 
'Sri Damansara': [3.1926° N, 101.6105° E], 
'Segambut': [3.1917° N, 101.6734° E], 
'Bukit Tunku': [3.1665° N, 101.6828° E], 
'Pantai': [3.1114° N, 101.6622° E], 
'OUG': [3.0726° N, 101.6731° E], 
'Desa Pandan': [3.1470° N, 101.7373° E], 
'Pandan Jaya': [3.1354° N, 101.7401° E], 
'Taman Tun Dr Ismail': [3.1461° N, 101.6255° E], 
'KL Sentral': [3.1342° N, 101.6861° E], 
'Keramat': [3.1689° N, 101.7277° E], 
'Bandar Damai Perdana': [3.0473° N, 101.7408° E], 
'Bukit Bintang': [3.1468° N, 101.7113° E], 
'Damansara': [3.0941° N, 101.5475° E], 
'Bandar Tasik Selatan': [3.0720° N, 101.7096° E], 
'Taman Duta': [3.1608° N, 101.6759° E], 
'Chan Sow Lin': [3.1278° N, 101.7156° E], 
'Pudu': [3.1348° N, 101.7136° E], 
'Kuchai Lama': [3.0839° N, 101.6883° E], 
'Seputeh': [3.1150° N, 101.6797° E], 
'Bangsar': [3.1290° N, 101.6798° E], 
'Sri Hartamas': [3.1600° N, 101.6520° E], 
'Mid Valley City': [3.1172° N, 101.6781° E], 
'Ampang Hilir': [3.1540° N, 101.7446° E], 
'Damansara Heights': [3.1491° N, 101.6534° E], 
'Desa ParkCity': [3.1862° N, 101.6299° E], 
'Jinjang': [3.2110° N, 101.6423° E], 
'Jalan Sultan Ismail': [None]
'Bukit Persekutuan': [3.1378° N, 101.6794° E], 
'Puchong': [3.0327° N, 101.6188° E], 
'Bandar Menjalara': [3.1939° N, 101.6309° E], 
'Pekan Batu': [3.2035° N, 101.6731° E], 
'Salak Selatan': [3.1049° N, 101.7055° E], 
'Sungai Penchala': [3.1620° N, 101.6245° E], 
'KL Eco City': [None]
'Batu': [2.7023° N, 101.5475° E], 
'Serdang': [5.2101° N, 100.6124° E], 
'Bukit Ledang': [None]
'Country Heights Damansara': [3.1784° N, 101.6211° E], 
'Country Heights': [2.9935° N, 101.7403° E], 
'Setia Eco Park': [3.1121° N, 101.4765° E], 
"""
