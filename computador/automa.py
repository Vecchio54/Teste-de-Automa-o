from netmiko import ConnectHandler
import keyring

# variaveis

usuario = "on"
password = keyring.get_password("cisco","rdo")

print (password)

# Funções

def altera_vlan(ip_sw, port_sw, v_dados, v_voz):
    warning = "trunk"
    show_config = [f"do sh running-config interface {port_sw}"]
    lista_comandos = [f"inteface {port_sw}", f"switchport access vlan {v_dados}",
                      f"switchport voice vlan {v_voz}", "shutdown", "no shutdown"]

    device_template = {
        'device_type':'cisco_ios',
        'host': ip_sw,
        'username': usuario,
        'password': password,
    }

    conectar = connectHandler(**device_template)
    show_port = conectar.send_config_set(show_config)
    if warning in show_port:
        return False
    else:
        comandos = conectar.send_config_set(lista_comandos)
        return True



