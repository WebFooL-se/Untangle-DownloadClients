#!/usr/bin/python -u
import sys
import uvm
import os

uvm = uvm.Uvm().getUvmContext()

nodeManager = uvm.nodeManager()
app = nodeManager.node("untangle-node-openvpn")
print app

appData = app.getSettings()
for client in appData['remoteClients']['list']:
    name = client['name']
    clientLink = app.getClientDistributionDownloadLink(name,"ovpn")
    result = os.system("wget -t 1 --content-disposition --timeout=3 http://localhost"+clientLink)
