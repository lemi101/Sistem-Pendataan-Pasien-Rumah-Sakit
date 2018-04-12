import json, socket, threading, xmlrpc.server
import paho.mqtt.client as mqtt_client

list_pasien = [
    {
        'nik' : 123,
        'nama' : 'Luthfi',
        'alamat' : 'Dinoyo',
        'penyakit' :  'Anemia'
    },
    {
        'nik' : 234,
        'nama' : 'Nanda',
        'alamat' : 'Setaman',
        'penyakit' :  'Diabetes'
    }
]

print('Subscriber MQTT di 127.0.0.1 di port 1883')
print('Topik : /rumah_sakit/pasien\n')

sub = mqtt_client.Client()

sub.connect('127.0.0.1', port=1883)

def add_pasien(nik, nama, alamat, penyakit):
    pasien = {
        'nik' : nik, 
        'nama' : nama, 
        'alamat' : alamat, 
        'penyakit' : penyakit
    }
        
    list_pasien.append(pasien)

    pasien = json.dumps(pasien)
    sub.publish('/rumah_sakit/pasien', pasien)

    return 'OK'

def get_pasien():
        data = json.dumps(list_pasien)
        return data

def handle_server(server):
    print('Server RPC di 127.0.0.1 di port 6667')

    server.register_function(add_pasien, "add_pasien")
    server.register_function(get_pasien, "get_pasien")

    server.serve_forever()


server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 6667) )    
t = threading.Thread(target=handle_server, args=(server,))
t.start()

def handle_message(client, object, msg):
    data = msg.payload.decode('ascii')
    data = json.loads(data)

    print('Data Pasien Baru diterima!\n')

    list_pasien.append(data)
    print('Data Pasien berhasil di Update!')

sub.on_message = handle_message

sub.subscribe('/rumah_sakit/pasien')

sub.loop_forever()