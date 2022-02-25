#Biblioetas
import socket
from os import system
from datetime import datetime
#Variaveis
info_ports = []


V = '\033[1;32m'  #verde
b = '\033[1;97m'  #branco
Y = "\033[1;33m"  #amarelo
c = '\033[1;36m'  #cian escuro
cc = '\033[1;96m' #cian claro
v = '\033[1;31m' #vermelho

#Menu
def menu():
  system('clear') or None
  print(f"""
     {c} +--^----------,--------,-----,--------^-,
      |  {v}|||||||||   --------      |         O
     {c} +---------------------------^----------|
     {c} \_,---------,---------,--------------'
      / {v}XXXXXX{c} /'|       /'    
      / {v}XXXXXX{c} /   \    /'
      / {v}XXXXXX{c} / _______/                
      / {v}XXXXXX{c} /
      / {v}XXXXXX{c} /
      (________( {cc}https://github.com/N3w-elf{cc}
      ____________________________
      |                          |
      |     [{v}01{c}] {v}- {c}Scan TCP{b}      {c}|
      |     [{v}02{c}] {v}- {c}Full Scan{b}     {c}|
      |__________________________|
    """)
  try:
    cmd = int(input(f"{Y}--->{b} "))
    ip = str(input(f"{c}IP do alvo: {v}"))

    if cmd == 1:
      ports = range(0, 1001)
      tcps(ip, ports)
    elif cmd == 2:
      ports = range(0, 65535)
      full(ip, ports)
    elif cmd >= 3 or cmd <= 0:
      exit()
  except:
    exit()
    print(f'{v}[!] - ERRO NA SELECAO DE OPÇÃO...')

def output(info_ports, ip): 
  #Pegando o horrario atual 
  hora = datetime.now().hour 
  minutos = datetime.now().minute 
  hrs = f'{hora}:{minutos}' 
  # Crinado o output 
  file = f'''{ip}-{hrs}.txt'''
  output_file = open(file, 'w') 
  for item in info_ports:
    output_file.write(item)
    output_file('\n')
  output_file.close()
  print(f'[*] - {Y}Output Salvo Em: {file}') 
  # SCAN NORMAL (OPÇAO: 1)
  # 37.59.174.225
def tcps(ip, ports):
  try:
    print(f"{c}PORTAS ABERTAS:\n")
    for port in ports:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      res = sock.connect_ex((ip, port))
      sock.close()
      if (res == 0):
        # Output--------------------------------------------------
        version= getversion(ip, port);
        info = f"{port} [ABERTA] - {version} "
        info_ports.append(info)
        # --------------------------------------------------------
        print(f"{port} [{V}ABERTA{c}] - {V} {version}{c} ", end='')
    output(info_ports, ip)
    input(f"[*] - {Y}Pressione enter para voltar ao menu.")
    menu()
  except:
      exit()
      print(f'{v}[!] IP OU SOCKET INVALIDO!')

# SCAN EM TODAS AS PORTAS (OPÇAO: 2)
def full(ip, ports):
  try:
    print("PORTAS ABERTAS:\n")
    for port in ports:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      res = sock.connect_ex((ip, port))
      sock.close()
      if (res == 0):
        # Output--------------------------------------------------
        version = version(ip, port);
        info = f"{port} [ABERTA] - {version} "
        info_ports.append(info)
        # --------------------------------------------------------
        print(f"{port} [{V}ABERTA{b}]", end='')
        getversion(ip, port)
    output(info_ports, ip)
    input(f"[*] - {Y}Pressione enter para voltar ao menu.")
    menu()

  except:
      exit()
      print(f'{v}[!] IP OU SOCKET INVALIDO!')

# CAPTURA O BANNER
def getversion(ip, port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((ip, port)); sock.settimeout(5.0); version = sock.recv(1024).decode('ascii'); sock.close(); return version
	except :
		print('Indetectavel'); return 'Indetectavel'