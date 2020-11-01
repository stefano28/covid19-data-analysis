import urllib, json
import urllib.request
import datetime

def read():
    stats = {'time': [], 'intensive_care': [], 'hospitalizations': []}
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        response = url.read()
        data = json.loads(response.decode('utf-8'))
        i = 0
        for dic in data:
            time = dic['data'].split('T')
            stats['hospitalizations'].append(int(dic['ricoverati_con_sintomi']))
            stats['intensive_care'].append(int(dic['terapia_intensiva']))
            stats['time'].append(time[0])
            i = i + 1
    return stats