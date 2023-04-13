#  **************************************************************************************
# *                    
# *                     Copyright (C) 2021 - 2023, Barca, Inc.
# *     
# *     
# *            GitHub: @BarcaWebCloud  |   E-Mail: <opensource@barca.com>                                           
# *
# *  This software is licensed as described in the file COPYING, which
# *  you should have received as part of this distribution. The terms are
# *  also available at https://project-barca.github.io/docs/copyright.html.
# *  You may opt to use, copy, modify, merge, publish, distribute and/or sell             
# *  copies of the Software, and permit persons to whom the Software is                   
# *  furnished to do so, under the terms of the COPYING file.                             
# *
# *  This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY            
# *  KIND, either express or implied.
# *
# *                            
# * **************************************************************************************

#!/usr/bin/python
import os
import sys, traceback

def start():
    try:
      print('''
     	                 
        BSCONF by Barca, Inc.
      	\n
      	Selecione alguma das opções abaixo
      ''')
      def optionFirst():
        while True:
          print ('''
          1) Instalar/Configurar Servidores
          2) Instalar por Categorias
          3) Desinstalar
          4) Ajuda

        ''')

          optionFirst = input("bsconf> ")
        
          while optionFirst == "1":
            print ('''
              Selecione o servidor:
              \n
              1) NGINX                       15) HFS
              2) Apache2                     16) IBM
              3) AOLserver                   17) Lighttpd
              4) Apache Tomcat               18) LiteSpeed
              5) Apache2                     19) Microsoft IIS
              6) Caudium                     20) OpenBSD
              8) Caddy                       21) Oracle iPlanet
              9) CERN httpd                  22) Oracle WebLogic
              10) GlassFish                  23) Xitami
              11) Hiawatha                   24) XAMPP
              12) Hiawatha                   25) WEBrick
              \n
              0) Instalar todos servidores   
              \n
              Digite 'back' para voltar     
            ''')
            _server = input("bsconf> ")
            if _server == "1":
              _version_server = input("\033[1;32mDeseja especificar a versão NGINX ? [y/n]> \033[1;m")
              if _version_server == "y":
                print("List all versions para NGINX")
            elif _server == "2":
              print('todo')
            elif _server == "3":
              print('todo')
            elif _server == "4":
              print('todo')
            elif _server == "5":
              print('todo')
            elif _server == "6":
              print('todo')
            elif _server == "7":
              print('todo')
            elif _server == "8":
              print('todo')
            elif _server == "9":
              print('todo')
            elif _server == "10":
              print('todo')
            elif _server == "11":
              print('todo')
            elif _server == "12":
              print('todo')
            elif _server == "13":
              print('todo')  
            elif _server == "14":
              print('todo')
            elif _server == "15":
              print('todo')
            elif _server == "16":
              print('todo') 
            elif _server == "17":
              print('todo')
            elif _server == "18":
              print('todo')
            elif _server == "19":
              print('todo')
            elif _server == "20":
              print('todo')
            elif _server == "21":
              print('todo')  
            elif _server == "22":
              print('todo')
            elif _server == "23":
              print('todo')
            elif _server == "24":
              print('todo') 
            elif _server == "25":
              print('todo')  
            elif _server == "back":
              optionFirst = 0
            elif _server == "home":
              optionFirst()
            else:
              print ("Desculpe, este comando é inválido ")
          if optionFirst == "3":
            print('todo')
          elif optionFirst == "4"	:
            print('todo')

          def categories():
            while optionFirst == "2":
              print ('''
                **************************** Categories *****************************

                1) Servidor Web HTTP				             9) Servidores de Arquivos
                2) Servidor de Email				             10) Servidores Proxy
                3) Servidor de Backup				             11) Servidor de Impressão
                4) Servidor de Banco de Dados            12) Servidor de Fax
                5) Servidor de DNS                       13) Servidor FTP
                6) Servidor de Aplicação                 14) Servidor de Virtualização
                7) Servidor de Imagens                   15) Servidor de Sistema Operacional:
                \n
                0) Todos 
                \n
                Digite 'back' para voltar    
                Digite 'home' para início
              ''')
              print ("Selecione uma categoria ou pressione (0) para instalar todas as ferramentas Kali Linux.\n")

              opcion1 = input("bsconf> ")
              if opcion1 == "back":
                optionFirst()
              elif opcion1 == "home":
                optionFirst()
              elif opcion1 == "0":
                cmd = os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
              while opcion1 == "1":
                print ("todo")
                opcion2 = input("bsconf> ")
                if opcion2 == "1":
                  print ("todo")
                elif opcion2 == "2":
                  print ("todo")
                elif opcion2 == "3":
                  print ("todo")
                elif opcion2 == "4":
                  print ("todo")
                elif opcion2 == "5":
                  print ("todo")
                elif opcion2 == "6":
                  print ("todo")
                elif opcion2 == "7":
                  print ("todo")
                elif opcion2 == "8":
                  print ("todo")
                elif opcion2 == "9":
                  print ("todo")
                elif opcion2 == "10":
                  print ("todo")
                elif opcion2 == "11":
                  print ("todo")
                elif opcion2 == "12":
                  print ("todo")
                elif opcion2 == "13":
                  print ("todo")
                elif opcion2 == "14":
                  print ("todo")
                elif opcion2 == "15":
                  print ("todo")
                elif opcion2 == "back":
                  inicio()
                elif opcion2 == "home":
                  optionFirst()		
                elif opcion2 == "0":
                  print ("todo")
                else:
                  print ("Opa! Comando inválido")
          categories()
      optionFirst()
    except KeyboardInterrupt:
      print ("Bye bye!")
    except Exception:
      traceback.print_exc(file=sys.stdout)
    sys.exit(0)
if __name__ == "__main__":
  start()