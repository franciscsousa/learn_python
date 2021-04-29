parsed="""AxisFault
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

parsed2="""AxisFault
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
with open('6021-totem-calcard-2021-02-11.log','r') as arquivo :
    log=arquivo.read()
log=log.replace(parsed," ")
log=log.replace(parsed2," ")
#print(type(log))
arq2=open('6021-totem-calcard-2021-02-11_NOVO.log','w')
arq2.write(log)

