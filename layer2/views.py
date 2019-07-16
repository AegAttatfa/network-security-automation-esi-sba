from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
import pprint
from netmiko import ConnectHandler

from .models import Device, Interface


def connect(self):
    pass
    '''
    devices = Device.objects.all()
    print(devices)
    for device in devices:
        print("The hostname " + device.hostname)
        net_connect = ConnectHandler(device_type=device.device_type,
                                     ip=device.ip_vlan,
                                     username=device.username,
                                     password=device.password)
        output = net_connect.send_command("show interfaces | i (.* line protocol is )|(.* address is)",
                                          use_textfsm=True)
        pprint.pprint(output)
        for int in output:
            interface = Interface(name_int=int["interface"],
                                  mac=int["address"],
                                  status=int["link_status"],
                                  mode="access",
                                  device=device
                                  )
            interface.save()
            print("savd")
'''


def device_get_interfaces(request, hostname):
    print("Getting ...")
    interfaces = Interface.objects.filter(device__hostname=hostname).order_by('name_int')
    return render(request, 'layer2/interfaces.html', {'interfaces': interfaces})


def device_list_view(request):
    devices = Device.objects.all()
    return render(request, 'layer2/listDevices.html', {'devices': devices})


def device_detail_view(request, hostname):
    device = get_object_or_404(Device, hostname=hostname)
    return render(request, 'layer2/deviceDetail.html', {'device': device})


def port_security(request):
    return render(request, 'layer2/index.html')
