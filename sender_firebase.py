# -*- coding: utf-8 -*-


import requests
from firebase import firebase

def foo():
    f = firebase.FirebaseApplication('https://myfireapptest-bf83f.firebaseio.com/')
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
    print(my_ip)
    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    x = {
    "latitude": geo_data["latitude"],
    "longitude": geo_data["longitude"],
    "isSleeping": "no"
    }
    print(x)
    f.post('/data',x)
    print("geolocation data posted")
    
def foo_sleep_status():
    f = firebase.FirebaseApplication('https://myfireapptest-bf83f.firebaseio.com/')
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
    print(my_ip)
    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()
    x = {
    "latitude": geo_data["latitude"],
    "longitude": geo_data["longitude"],
    "isSleeping": "yes"
    }
    print(x)
    f.post('/data',x)
    print("geolocation data posted")