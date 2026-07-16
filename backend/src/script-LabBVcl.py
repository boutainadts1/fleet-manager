#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import libvirt
import os

# Empêcher affichage erreurs libvirt
def libvirt_callback(userdata, err):
    pass
libvirt.registerErrorHandler(f=libvirt_callback, ctx=None)

# Connexion
conn = libvirt.open("qemu:///system")
if not conn:
    raise SystemExit("Connexion impossible à KVM !")


# ----------- MENU -----------
def menu():
    print("\nProgramme de gestion des machines virtuelles ; veuillez entrer votre choix")
    print("0) Nom de la machine hyperviseur")
    print("1) Créer une machine virtuelle")
    print("2) Lister les machines virtuelles")
    print("3) Démarrer une machine")
    print("4) Arrêter une machine")
    print("5) L’adresse IP d’une machine virtuelle donnée")
    print("6) Quitter")


# ----------- CREATION VM -----------
def creer_vm():
    print("\n--- Création d'une nouvelle machine virtuelle ---")
    nom = raw_input("Nom de la VM : ")
    iso = raw_input("Chemin ISO (ex: /ISO/ubuntu.iso) : ")
    taille = raw_input("Taille du disque en Go : ")

    disk_path = "/var/lib/libvirt/images/{}.qcow2".format(nom)
    os.system("qemu-img create -f qcow2 {} {}G".format(disk_path, taille))

    xml = """
<domain type='kvm'>
  <name>{}</name>
  <memory unit='MiB'>1024</memory>
  <vcpu placement='static'>1</vcpu>

  <os>
    <type arch='x86_64'>hvm</type>
    <boot dev='cdrom'/>
  </os>

  <devices>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='{}'/>
      <target dev='vda' bus='virtio'/>
    </disk>

    <disk type='file' device='cdrom'>
      <source file='{}'/>
      <target dev='hda' bus='ide'/>
      <readonly/>
    </disk>

    <interface type='network'>
      <source network='default'/>
    </interface>

    <graphics type='vnc' port='-1'/>
  </devices>
</domain>
""".format(nom, disk_path, iso)

    try:
        conn.defineXML(xml)
        print("VM créée avec succès !")
    except libvirt.libvirtError as e:
        print("Erreur création VM :", str(e))


# ----------- LISTE MACHINES -----------
def liste_vm():
    vms = conn.listAllDomains()
    if len(vms) == 0:
        print("\nAucune VM trouvée.")
    else:
        print("\nListe des machines virtuelles :")
        for vm in vms:
            state = vm.state()[0]
            txt = "allumée" if state == libvirt.VIR_DOMAIN_RUNNING else "éteinte"
            print(" - {}  ({})".format(vm.name(), txt))


# ----------- DEMARRER VM -----------
def demarrer_vm():
    vms = conn.listAllDomains()
    print("\nMachines disponibles :")
    for i, vm in enumerate(vms):
        print("{} - {}".format(i, vm.name()))

    choix = int(raw_input("Choisir la machine à démarrer : "))
    try:
        vm = vms[choix]
        vm.create()
        print("Machine démarrée.")
    except:
        print("Erreur : choix invalide.")


# ----------- ARRETER VM -----------
def arreter_vm():
    vms = conn.listAllDomains()
    print("\nMachines disponibles :")
    for i, vm in enumerate(vms):
        print("{} - {}".format(i, vm.name()))

    choix = int(raw_input("Choisir la machine à arrêter : "))
    try:
        vm = vms[choix]
        vm.shutdown()
        print("Machine arrêtée.")
    except:
        print("Erreur : choix invalide.")


# ----------- ADRESSE IP -----------
def ip_vm():
    nom = raw_input("Nom de la VM : ")
    try:
        vm = conn.lookupByName(nom)
    except:
        print("Machine introuvable.")
        return

    if not vm.isActive():
        print("La machine est éteinte, impossible de lire l’adresse IP.")
        return

    try:
        ifaces = vm.interfaceAddresses(
            libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0
        )
    except:
        print("QEMU Guest Agent non installé !")
        return

    print("\nAdresse(s) IP de la machine", nom)
    for (name, val) in ifaces.items():
        if name != "lo" and val['addrs']:
            for addr in val['addrs']:
                if addr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                    print("→", addr['addr'])


# ----------- BOUCLE PRINCIPALE -----------
choix = -1

while choix != 6:
    menu()
    try:
        choix = int(raw_input("Votre choix : "))
    except:
        choix = -1

    if choix == 0:
        print("\nNom hyperviseur :", conn.getHostname())

    elif choix == 1:
        creer_vm()

    elif choix == 2:
        liste_vm()

    elif choix == 3:
        demarrer_vm()

    elif choix == 4:
        arreter_vm()

    elif choix == 5:
        ip_vm()

    elif choix == 6:
        print("Fermeture du programme...")

    else:
        print("Choix invalide.")

conn.close()
