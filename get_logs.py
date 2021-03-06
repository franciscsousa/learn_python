# -*- coding: utf-8 -*-
import requests
import sys
import argparse
import datetime
import mysql
import os
import platform
#from os import error
import connector
from connector import errorcode
import json
import csv



def main() :
	if platform.system() == 'Windows':
		ping='ping -n 1 '
		terminal_saida=' > null'
	else:
		ping='ping -c 1 '
		terminal_saida=' > /dev/null'
	parser = argparse.ArgumentParser(description='teste arg')
	parser.add_argument('--serial',"--s", default='', help= "Digite o Número de Série do totem que será coletado.")
	parser.add_argument('--date', "--d", default='', help= "Digite a data de coleta dos Logs AAAA-MM-DD")
	parser.add_argument('--db', "--b", default='', help= "Se deseja apenas consultar o banco de dados.") 
	args = parser.parse_args()
	if args.serial=='':
		print("Digite um número de série para realizar a coleta de logs...")
		return 0
	else:		
		if os.path.isfile('tabelatotens.csv'):
			with open('tabelatotens.csv', mode='r', encoding='utf-8') as csv_file:
				terminais = csv.DictReader(csv_file, delimiter=';')
				print(f"Pesquisando Host para o serial { args.serial }")
				for terminal in terminais:
					if terminal["Serial"]==args.serial:
						host=terminal["IP"]
						print(f'Buscando acesso ao IP.:{host}')
						retorno = os.system(ping + host + terminal_saida )
						if retorno == 0:						
							if not args.db:
								get_log(host, args.date,"totem-calcard",args.serial)
								get_log(host, args.date,"vs-auto-pag-se",args.serial)
								get_log(host, args.date,"vs-conductor",args.serial)
								get_log(host, args.date,"vscontrol-agent",args.serial)
								get_dmp(host, args.date, args.serial)
							dbselect(host, "totem_calcard", args.serial)
						else:
							print("Sem acesso ao totem selecionado. Por favor tente mais tarde.")


def get_db(host) :
	dbconnect(host, 'root', 'root')
	db_query('select * from totem.calcard.card;')

def get_dmp (host, date,serial):
	if date=='':
		date=str(datetime.date.today())
	date=date.replace('-','')
	print(f'Data de coleta é... {date}')
	if serial!='':
		serial=serial+'-'
	#http://172.16.106.150/get-dmp.php?arq=CliSiTef.20201028.dmp
	try:
		response=requests.get('http://'+host+'/get-dmp.php?arq=CliSiTef.'+date+'.dmp', allow_redirects=False)
#	except ConnectionError:
	except requests.HTTPError:
		print(f'Não foi possível salvar o arquivo Clisitef.{date}.dmp. Verifique a conexão ou o dia solicitado.')
		return 0
	except requests.Timeout: 
		print(f'Não foi possível salvar o arquivo Clisitef.{date}.dmp. Tempo máximo de conexão atingindo.')
		return 0
	except requests.ConnectionError:
		print(f'Não foi possível salvar o arquivo Clisitef.{date}.dmp. Falhou ao estabelecer uma conexão.')
	else:		
		arquivo=open(serial+'Clisitef.'+date+'.dmp', 'wb')
		arquivo.write(response.content)
		arquivo.close()

def get_log(host, date, arq, serial):
	texto1="""AxisFault
 faultCode: {http://xml.apache.org/axis/}HTTP
 faultSubcode: 
 faultString: (502)Bad Gateway
 faultActor: 
 faultNode: 
 faultDetail: 
	{}:return code:  502
&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.1//EN&quot; &quot;http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd&quot;&gt;

&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot; xml:lang=&quot;en&quot;&gt;
    &lt;head&gt;
        &lt;title&gt;The page is temporarily unavailable&lt;/title&gt;
        &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;
        &lt;style type=&quot;text/css&quot;&gt;
            /*&lt;![CDATA[*/
            body {
                background-color: #fff;
                color: #000;
                font-size: 0.9em;
                font-family: sans-serif,helvetica;
                margin: 0;
                padding: 0;
            }
            :link {
                color: #c00;
            }
            :visited {
                color: #c00;
            }
            a:hover {
                color: #f50;
            }
            h1 {
                text-align: center;
                margin: 0;
                padding: 0.6em 2em 0.4em;
                background-color: #294172;
                color: #fff;
                font-weight: normal;
                font-size: 1.75em;
                border-bottom: 2px solid #000;
            }
            h1 strong {
                font-weight: bold;
                font-size: 1.5em;
            }
            h2 {
                text-align: center;
                background-color: #3C6EB4;
                font-size: 1.1em;
                font-weight: bold;
                color: #fff;
                margin: 0;
                padding: 0.5em;
                border-bottom: 2px solid #294172;
            }
            h3 {
                text-align: center;
                background-color: #ff0000;
                padding: 0.5em;
                color: #fff;
            }
            hr {
                display: none;
            }
            .content {
                padding: 1em 5em;
            }
            .alert {
                border: 2px solid #000;
            }

            img {
                border: 2px solid #fff;
                padding: 2px;
                margin: 2px;
            }
            a:hover img {
                border: 2px solid #294172;
            }
            .logos {
                margin: 1em;
                text-align: center;
            }
            /*]]&gt;*/
        &lt;/style&gt;
    &lt;/head&gt;

    &lt;body&gt;
        &lt;h1&gt;&lt;strong&gt;nginx error!&lt;/strong&gt;&lt;/h1&gt;

        &lt;div class=&quot;content&quot;&gt;

            &lt;h3&gt;The page you are looking for is temporarily unavailable.  Please try again later.&lt;/h3&gt;

            &lt;div class=&quot;alert&quot;&gt;
                &lt;h2&gt;Website Administrator&lt;/h2&gt;
                &lt;div class=&quot;content&quot;&gt;
                    &lt;p&gt;Something has triggered an error on your
                    website.  This is the default error page for
                    &lt;strong&gt;nginx&lt;/strong&gt; that is distributed with
                    Fedora.  It is located
                    &lt;tt&gt;/usr/share/nginx/html/50x.html&lt;/tt&gt;&lt;/p&gt;

                    &lt;p&gt;You should customize this error page for your own
                    site or edit the &lt;tt&gt;error_page&lt;/tt&gt; directive in
                    the &lt;strong&gt;nginx&lt;/strong&gt; configuration file
                    &lt;tt&gt;/etc/nginx/nginx.conf&lt;/tt&gt;.&lt;/p&gt;

                &lt;/div&gt;
            &lt;/div&gt;

            &lt;div class=&quot;logos&quot;&gt;
                &lt;a href=&quot;http://nginx.net/&quot;&gt;&lt;img
                    src=&quot;/nginx-logo.png&quot;
                    alt=&quot;[ Powered by nginx ]&quot;
                    width=&quot;121&quot; height=&quot;32&quot; /&gt;&lt;/a&gt;

                &lt;a href=&quot;http://fedoraproject.org/&quot;&gt;&lt;img 
                    src=&quot;/poweredby.png&quot;
                    alt=&quot;[ Powered by Fedora ]&quot; 
                    width=&quot;88&quot; height=&quot;31&quot; /&gt;&lt;/a&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;
&lt;/html&gt;

	{http://xml.apache.org/axis/}HttpErrorCode:502

(502)Bad Gateway
	at org.apache.axis.transport.http.HTTPSender.readFromSocket(HTTPSender.java:744)
	at org.apache.axis.transport.http.HTTPSender.invoke(HTTPSender.java:144)
	at org.apache.axis.strategies.InvocationStrategy.visit(InvocationStrategy.java:32)
	at org.apache.axis.SimpleChain.doVisiting(SimpleChain.java:118)
	at org.apache.axis.SimpleChain.invoke(SimpleChain.java:83)
	at org.apache.axis.client.AxisClient.invoke(AxisClient.java:165)
	at org.apache.axis.client.Call.invokeEngine(Call.java:2784)
	at org.apache.axis.client.Call.invoke(Call.java:2767)
	at org.apache.axis.client.Call.invoke(Call.java:2443)
	at org.apache.axis.client.Call.invoke(Call.java:2366)
	at org.apache.axis.client.Call.invoke(Call.java:1812)
	at br.com.videosoft.vscontrol.report.webservice.Application_Webservice_ReportWebserviceBindingStub.saveReports(Application_Webservice_ReportWebserviceBindingStub.java:107)
	at br.com.videosoft.vscontrol.report.webservice.ReportWebservice.saveReports(ReportWebservice.java:12)
	at br.com.videosoft.vscontrol.report.agent.WebserviceReportServer.sendReport(WebserviceReportServer.java:35)
	at br.com.videosoft.vscontrol.report.agent.ReportAgent.sendReports(ReportAgent.java:139)
	at br.com.videosoft.totemcalcard.reportagent.ReportVsControl.run(ReportVsControl.java:59)
	at br.com.videosoft.totemcalcard.common.ApplicationParam.processParams(ApplicationParam.java:80)
	at br.com.videosoft.totemcalcard.Main.main(Main.java:79)"""

	texto2="""AxisFault
 faultCode: {http://xml.apache.org/axis/}HTTP
 faultSubcode: 
 faultString: (504)Gateway Time-out
 faultActor: 
 faultNode: 
 faultDetail: 
	{}:return code:  504
&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.1//EN&quot; &quot;http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd&quot;&gt;

&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot; xml:lang=&quot;en&quot;&gt;
    &lt;head&gt;
        &lt;title&gt;The page is temporarily unavailable&lt;/title&gt;
        &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;
        &lt;style type=&quot;text/css&quot;&gt;
            /*&lt;![CDATA[*/
            body {
                background-color: #fff;
                color: #000;
                font-size: 0.9em;
                font-family: sans-serif,helvetica;
                margin: 0;
                padding: 0;
            }
            :link {
                color: #c00;
            }
            :visited {
                color: #c00;
            }
            a:hover {
                color: #f50;
            }
            h1 {
                text-align: center;
                margin: 0;
                padding: 0.6em 2em 0.4em;
                background-color: #294172;
                color: #fff;
                font-weight: normal;
                font-size: 1.75em;
                border-bottom: 2px solid #000;
            }
            h1 strong {
                font-weight: bold;
                font-size: 1.5em;
            }
            h2 {
                text-align: center;
                background-color: #3C6EB4;
                font-size: 1.1em;
                font-weight: bold;
                color: #fff;
                margin: 0;
                padding: 0.5em;
                border-bottom: 2px solid #294172;
            }
            h3 {
                text-align: center;
                background-color: #ff0000;
                padding: 0.5em;
                color: #fff;
            }
            hr {
                display: none;
            }
            .content {
                padding: 1em 5em;
            }
            .alert {
                border: 2px solid #000;
            }

            img {
                border: 2px solid #fff;
                padding: 2px;
                margin: 2px;
            }
            a:hover img {
                border: 2px solid #294172;
            }
            .logos {
                margin: 1em;
                text-align: center;
            }
            /*]]&gt;*/
        &lt;/style&gt;
    &lt;/head&gt;

    &lt;body&gt;
        &lt;h1&gt;&lt;strong&gt;nginx error!&lt;/strong&gt;&lt;/h1&gt;

        &lt;div class=&quot;content&quot;&gt;

            &lt;h3&gt;The page you are looking for is temporarily unavailable.  Please try again later.&lt;/h3&gt;

            &lt;div class=&quot;alert&quot;&gt;
                &lt;h2&gt;Website Administrator&lt;/h2&gt;
                &lt;div class=&quot;content&quot;&gt;
                    &lt;p&gt;Something has triggered an error on your
                    website.  This is the default error page for
                    &lt;strong&gt;nginx&lt;/strong&gt; that is distributed with
                    Fedora.  It is located
                    &lt;tt&gt;/usr/share/nginx/html/50x.html&lt;/tt&gt;&lt;/p&gt;

                    &lt;p&gt;You should customize this error page for your own
                    site or edit the &lt;tt&gt;error_page&lt;/tt&gt; directive in
                    the &lt;strong&gt;nginx&lt;/strong&gt; configuration file
                    &lt;tt&gt;/etc/nginx/nginx.conf&lt;/tt&gt;.&lt;/p&gt;

                &lt;/div&gt;
            &lt;/div&gt;

            &lt;div class=&quot;logos&quot;&gt;
                &lt;a href=&quot;http://nginx.net/&quot;&gt;&lt;img
                    src=&quot;/nginx-logo.png&quot;
                    alt=&quot;[ Powered by nginx ]&quot;
                    width=&quot;121&quot; height=&quot;32&quot; /&gt;&lt;/a&gt;

                &lt;a href=&quot;http://fedoraproject.org/&quot;&gt;&lt;img 
                    src=&quot;/poweredby.png&quot;
                    alt=&quot;[ Powered by Fedora ]&quot; 
                    width=&quot;88&quot; height=&quot;31&quot; /&gt;&lt;/a&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;
&lt;/html&gt;

	{http://xml.apache.org/axis/}HttpErrorCode:504

(504)Gateway Time-out
	at org.apache.axis.transport.http.HTTPSender.readFromSocket(HTTPSender.java:744)
	at org.apache.axis.transport.http.HTTPSender.invoke(HTTPSender.java:144)
	at org.apache.axis.strategies.InvocationStrategy.visit(InvocationStrategy.java:32)
	at org.apache.axis.SimpleChain.doVisiting(SimpleChain.java:118)
	at org.apache.axis.SimpleChain.invoke(SimpleChain.java:83)
	at org.apache.axis.client.AxisClient.invoke(AxisClient.java:165)
	at org.apache.axis.client.Call.invokeEngine(Call.java:2784)
	at org.apache.axis.client.Call.invoke(Call.java:2767)
	at org.apache.axis.client.Call.invoke(Call.java:2443)
	at org.apache.axis.client.Call.invoke(Call.java:2366)
	at org.apache.axis.client.Call.invoke(Call.java:1812)
	at br.com.videosoft.vscontrol.report.webservice.Application_Webservice_ReportWebserviceBindingStub.saveReports(Application_Webservice_ReportWebserviceBindingStub.java:107)
	at br.com.videosoft.vscontrol.report.webservice.ReportWebservice.saveReports(ReportWebservice.java:12)
	at br.com.videosoft.vscontrol.report.agent.WebserviceReportServer.sendReport(WebserviceReportServer.java:35)
	at br.com.videosoft.vscontrol.report.agent.ReportAgent.sendReports(ReportAgent.java:139)
	at br.com.videosoft.totemcalcard.reportagent.ReportVsControl.run(ReportVsControl.java:59)
	at br.com.videosoft.totemcalcard.common.ApplicationParam.processParams(ApplicationParam.java:80)
	at br.com.videosoft.totemcalcard.Main.main(Main.java:79)"""

	texto3="""java.rmi.RemoteException: HTTP Status-Code 504: Gateway Time-out; nested exception is: 
	HTTP Status-Code 504: Gateway Time-out
	at br.com.videosoft.vscontrol.report.webservice.Application_Webservice_ReportWebservicePort_Stub.saveReports(Application_Webservice_ReportWebservicePort_Stub.java:89)
	at br.com.videosoft.vscontrol.report.webservice.ReportWebservice.saveReports(ReportWebservice.java:21)
	at br.com.videosoft.vsautopagse.reportagent.WebserviceReportServer.sendReport(WebserviceReportServer.java:36)
	at br.com.videosoft.vsautopagse.reportagent.ReportAgent.sendReports(ReportAgent.java:166)
	at br.com.videosoft.vsautopagse.reportagent.ReportAgent.run(ReportAgent.java:65)
	at br.com.videosoft.vsautopagse.util.ApplicationParam.processParams(ApplicationParam.java:219)
	at br.com.videosoft.vsautopagse.Main.main(Main.java:30)
Caused by: HTTP Status-Code 504: Gateway Time-out
	at com.sun.xml.rpc.client.http.HttpClientTransport.invoke(HttpClientTransport.java:135)
	at com.sun.xml.rpc.client.StreamingSender._send(StreamingSender.java:113)
	at br.com.videosoft.vscontrol.report.webservice.Application_Webservice_ReportWebservicePort_Stub.saveReports(Application_Webservice_ReportWebservicePort_Stub.java:72)
	... 6 more"""
	texto4="""AxisFault
 faultCode: {http://xml.apache.org/axis/}HTTP
 faultSubcode: 
 faultString: (504)Gateway Time-out
 faultActor: 
 faultNode: 
 faultDetail: 
	{}:return code:  504
&lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.1//EN&quot; &quot;http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd&quot;&gt;

&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot; xml:lang=&quot;en&quot;&gt;
    &lt;head&gt;
        &lt;title&gt;The page is temporarily unavailable&lt;/title&gt;
        &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;
        &lt;style type=&quot;text/css&quot;&gt;
            /*&lt;![CDATA[*/
            body {
                background-color: #fff;
                color: #000;
                font-size: 0.9em;
                font-family: sans-serif,helvetica;
                margin: 0;
                padding: 0;
            }
            :link {
                color: #c00;
            }
            :visited {
                color: #c00;
            }
            a:hover {
                color: #f50;
            }
            h1 {
                text-align: center;
                margin: 0;
                padding: 0.6em 2em 0.4em;
                background-color: #294172;
                color: #fff;
                font-weight: normal;
                font-size: 1.75em;
                border-bottom: 2px solid #000;
            }
            h1 strong {
                font-weight: bold;
                font-size: 1.5em;
            }
            h2 {
                text-align: center;
                background-color: #3C6EB4;
                font-size: 1.1em;
                font-weight: bold;
                color: #fff;
                margin: 0;
                padding: 0.5em;
                border-bottom: 2px solid #294172;
            }
            h3 {
                text-align: center;
                background-color: #ff0000;
                padding: 0.5em;
                color: #fff;
            }
            hr {
                display: none;
            }
            .content {
                padding: 1em 5em;
            }
            .alert {
                border: 2px solid #000;
            }

            img {
                border: 2px solid #fff;
                padding: 2px;
                margin: 2px;
            }
            a:hover img {
                border: 2px solid #294172;
            }
            .logos {
                margin: 1em;
                text-align: center;
            }
            /*]]&gt;*/
        &lt;/style&gt;
    &lt;/head&gt;

    &lt;body&gt;
        &lt;h1&gt;&lt;strong&gt;nginx error!&lt;/strong&gt;&lt;/h1&gt;

        &lt;div class=&quot;content&quot;&gt;

            &lt;h3&gt;The page you are looking for is temporarily unavailable.  Please try again later.&lt;/h3&gt;

            &lt;div class=&quot;alert&quot;&gt;
                &lt;h2&gt;Website Administrator&lt;/h2&gt;
                &lt;div class=&quot;content&quot;&gt;
                    &lt;p&gt;Something has triggered an error on your
                    website.  This is the default error page for
                    &lt;strong&gt;nginx&lt;/strong&gt; that is distributed with
                    Fedora.  It is located
                    &lt;tt&gt;/usr/share/nginx/html/50x.html&lt;/tt&gt;&lt;/p&gt;

                    &lt;p&gt;You should customize this error page for your own
                    site or edit the &lt;tt&gt;error_page&lt;/tt&gt; directive in
                    the &lt;strong&gt;nginx&lt;/strong&gt; configuration file
                    &lt;tt&gt;/etc/nginx/nginx.conf&lt;/tt&gt;.&lt;/p&gt;

                &lt;/div&gt;
            &lt;/div&gt;

            &lt;div class=&quot;logos&quot;&gt;
                &lt;a href=&quot;http://nginx.net/&quot;&gt;&lt;img
                    src=&quot;/nginx-logo.png&quot;
                    alt=&quot;[ Powered by nginx ]&quot;
                    width=&quot;121&quot; height=&quot;32&quot; /&gt;&lt;/a&gt;

                &lt;a href=&quot;http://fedoraproject.org/&quot;&gt;&lt;img 
                    src=&quot;/poweredby.png&quot;
                    alt=&quot;[ Powered by Fedora ]&quot; 
                    width=&quot;88&quot; height=&quot;31&quot; /&gt;&lt;/a&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/body&gt;
&lt;/html&gt;

	{http://xml.apache.org/axis/}HttpErrorCode:504

(504)Gateway Time-out
	at org.apache.axis.transport.http.HTTPSender.readFromSocket(HTTPSender.java:744)
	at org.apache.axis.transport.http.HTTPSender.invoke(HTTPSender.java:144)
	at org.apache.axis.strategies.InvocationStrategy.visit(InvocationStrategy.java:32)
	at org.apache.axis.SimpleChain.doVisiting(SimpleChain.java:118)
	at org.apache.axis.SimpleChain.invoke(SimpleChain.java:83)
	at org.apache.axis.client.AxisClient.invoke(AxisClient.java:165)
	at org.apache.axis.client.Call.invokeEngine(Call.java:2784)
	at org.apache.axis.client.Call.invoke(Call.java:2767)
	at org.apache.axis.client.Call.invoke(Call.java:2443)
	at org.apache.axis.client.Call.invoke(Call.java:2366)
	at org.apache.axis.client.Call.invoke(Call.java:1812)
	at br.com.videosoft.vscontrol.report.webservice.Application_Webservice_ReportWebserviceBindingStub.saveReports(Application_Webservice_ReportWebserviceBindingStub.java:107)
	at br.com.videosoft.vscontrol.report.webservice.ReportWebservice.saveReports(ReportWebservice.java:12)
	at br.com.videosoft.vscontrol.report.agent.WebserviceReportServer.sendReport(WebserviceReportServer.java:35)
	at br.com.videosoft.vscontrol.report.agent.ReportAgent.sendReports(ReportAgent.java:139)
	at br.com.videosoft.totemcalcard.reportagent.ReportVsControl.run(ReportVsControl.java:59)
	at br.com.videosoft.totemcalcard.common.ApplicationParam.processParams(ApplicationParam.java:80)
	at br.com.videosoft.totemcalcard.Main.main(Main.java:79)"""
	if serial=='':
		num_serie=''
	else:
		num_serie=serial+'-'
	msg='Não foi possível salvar log do arquivo '+arq+'.'
	try:
		response = requests.get('http://'+host+'/get-logs.php?app='+arq+'&date='+date)
	except requests.HTTPError:
		print(f'{msg} Verifique a conexão ou o dia solicitado.')
		return 0
	except requests.Timeout: 
		print(f'{msg} Tempo máximo de conexão atingindo.')
		return 0
	except requests.ConnectionError:
		print(f'{msg} Falhou ao estabelecer uma conexão.')
	else:
		if date=='':
			date=str(datetime.date.today())
		print(f'Coletando logs com data de {date} para o arquivo {arq}')
		arquivo=open(num_serie+arq+'-'+date+'.log','wt')
		#response.replace("<br />","")
		#saves=print(response.text)
		#saves.replace("<br />","")
		#print(saves)
		parsed=response.text
		parsed=parsed.replace('<br />','')
		parsed=parsed.replace(texto1,'')
		parsed=parsed.replace(texto2,'')
		parsed=parsed.replace(texto3,'')
		arquivo.write(parsed)
		arquivo.close()
	return 0

def dbconnect(dbhost='localhost', user='root', password='root', database=None):
    status=1
    #print(f'Conectando no host {dbhost}, user: {user} password: {password}')
    print(f'Conectando ao Host: {dbhost} Banco de dados: {database}')
    try:
        db_connection = connector.connect(host=dbhost, user=user, password=password, database=database)
        #print("Conexão ao Banco de dados Realizada")
    except connector.Error as error:
        if error.errno == 1045:
            print("Acesso negado ao Banco de Dados.")
            return 0
        #if error.errno == errorcode.ER_BAD_DB_ERROR:
        #    print("Banco de Dados não existe")
        #elif error.errno == errorcode.ER.ACCESS_DENIED_ERROR:
        #    print("Nome de Usuário e/ou Senha errados")
        elif error.errno == 2003:
            print('Não foi possível conectar ao Banco de Dados no Host.')
            return 0
        else:
            return error
            #status=0
        #    print(error)
    else:
        return db_connection
    return

def dbselect(host,banco, serial) :
	date=str(datetime.date.today())
	date=date.replace('-','')
	banco=dbconnect(dbhost=host, user='root', password='root', database=banco)
	if banco != 0:
		mycursor = banco.cursor()
		mycursor.execute("select * from `totem_calcard`.`card` where PAYMENTCONFIRMPCHCOMPLETED = 0 AND PAYMENTCOMPLETED = 1 AND RENEGOTIATIONPROGRESS = 0;")

		myresult = mycursor.fetchall()
		indice=('id','balance', 'cardnumber', 'customer', 'payslip', 'paymentresult', 'printslip', 'printstatementaccount', 'releasecard', 'releasecardcompleted', 'reprintslip', 'statementaccount', 'utilization_id', 'renegotiationprogressconfirmed', 'renegotiationprogress', 'renegotiationsilmulate', 'accoundid', 'agreementid', 'cardid', 'cpfcarrier', 'integrationpaymentsap', 'paymentcompleted', 'paymentconfirmpchcompleted','paymentconfirmpchresult', 'refin')
		resultado={}
		contador=0
		arquivo=serial+'-dbdump-'+date+'.json'
		if (len(myresult)>0):
			for x in myresult:
				result={}
				for i in range(25):
					result.update({indice[i]:x[i]})
				mID = result[f"{indice[0]}"]
				transacao=result[f"{indice[5]}"]
				temp=transacao.find("ONL-C")
				dia_transacao=transacao[temp-19:temp]
				dia_transacao=dia_transacao.replace("     ", " ")
				temp=transacao.find("R$")
				valor_transacao=transacao[temp:]
				temp=valor_transacao.find(",")
				valor_transacao=valor_transacao[:temp+3]
				valor_transacao=valor_transacao.rstrip()
				mpchconfirm=result[f"{indice[22]}"]
				print(f"ID: {mID} \t Data e Horário {dia_transacao} \t Valor: {valor_transacao} \t PCH CONFIRMADO {mpchconfirm} \t")

				resultado.update({contador+1:result})
				contador = contador + 1
		else:
			resultado={"resultado":"Sem retorno do banco"}
		with open(arquivo, 'w') as saida:
			json.dump(resultado, saida)
	else: 
		print("Sem acesso ao banco de dados...")
	return

if __name__ == '__main__':
	sys.exit(main())

