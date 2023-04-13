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

def home():
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
              0) Instalar Todas
              \n
              Digite 'back' para voltar 
              Digite 'home' para início
              \n
              Pressione 'Ctrl+C' para sair 
            ''')
            _server = input("bsconf> ")
            if _server == "1":
              _version_server = input("\033[1;32mDeseja especificar a versão do NGINX ? [y/n]> \033[1;m")
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
              home()
            else:
              print ("Desculpe, este comando é inválido ")
          if optionFirst == "3":
            print('todo')
          elif optionFirst == "4"	:
            print('todo')
          # categories
          def categories():
            while optionFirst == "2":
              print ('''
                Selecione a categoria desejada:

                1) Servidor Web				             9) Servidores de Arquivos
                2) Servidor de Email				             10) Servidores Proxy
                3) Servidor de Backup				             11) Servidor de Impressão
                4) Servidor de Banco de Dados            12) Servidor de Fax
                5) Servidor de DNS                       13) Servidor FTP
                6) Servidor de Aplicação                 14) Servidor de Virtualização
                7) Servidor de Imagens                   15) Servidor de Sistema Operacional:
                \n
                0) Instalar Todas 
                \n
                Digite 'back' para voltar 
                Digite 'home' para início
                \n
                Pressione 'Ctrl+C' para sair
              ''')
              
              optionCategory = input("bsconf> ")
              if optionCategory == "back":
                home()
              elif optionCategory == "home":
                home()
              elif optionCategory == "0":
                print("todo:all")
              # web servers
              def listWebServer():
                while optionCategory == "1":
                  print ('''
                    Selecione o servidor:
                    \n
                    1) NGINX                       15) HFS
                    2) Jetty                       16) IBM
                    3) Abyss                       17) Zeus
                    4) AOLserver                   18) Lighttpd
                    5) Apache Tomcat               19) LiteSpeed
                    6) Apache2                     20) Microsoft IIS
                    7) Caudium                     21) OpenBSD
                    8) Caddy                       22) Oracle iPlanet
                    9) Klone                       23) Oracle WebLogic
                    10) CERN httpd                 24) Oracle Web Tier
                    11) GlassFish                  25) Xitami
                    12) Hiawatha                   26) XAMPP
                    13) Yaws                       27) Zope
                    14) Resin                      28) WEBrick
                    \n
                    0) Instalar Todas
                    \n
                    Digite 'back' para voltar 
                    Digite 'home' para início
                    \n
                    Pressione 'Ctrl+C' para sair 
                  ''')
                  
                  _optionwebServer = input("bsconf> ")
                  if _optionwebServer == "back":
                    categories()
                  elif _optionwebServer == "home":
                    home()
                  elif _optionwebServer == "0":
                    print("todo:all")
                  # nginx
                  def releasesNGINX():
                    while _optionwebServer == "1":
                      _version_server = input("Deseja especificar a versão do NGINX ? [y/n]> ")
                      if _version_server == "y":
                        print ('''
                          Selecione a versão desejada
                          \n
                          1) 1.22.1 (latest)             8) 1.6.3
                          2) 1.20.2                      9) 1.4.7
                          3) 1.18.0                      10) 1.2.9
                          4) 1.16.1                      11) 1.0.15
                          5) 1.14.2                      12) 0.8.55
                          6) 1.10.3                      13) 0.7.69
                          7) 1.8.1                       14) 0.5.38            
                          \n
                          Digite 'back' para voltar 
                          Digite 'home' para início
                          \n
                          Pressione 'Ctrl+C' para sair 
                        ''')
                        _releaseNGINX = input("bsconf> ")  
                        if _releaseNGINX == "1":
                          print("Instalando NGINX 1.22.1")
                        elif _releaseNGINX == "2":
                          print("Instalando NGINX 1.20.2")
                        elif _releaseNGINX == "back":
                          listWebServer()
                        elif _releaseNGINX == "home":
                          home()
                        else:
                          print("comando inválido")
                      else:
                        print("Instalando a versão mais rececnte...")
                  releasesNGINX()
              listWebServer()
          categories()
      optionFirst()
    except KeyboardInterrupt:
      print ("Bye bye!")
    except Exception:
      traceback.print_exc(file=sys.stdout)
    sys.exit(0)
if __name__ == "__main__":
  home()