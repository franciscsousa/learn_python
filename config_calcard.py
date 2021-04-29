###configuration.properties

serial=input('Digite o serial..: ')
print (serial)

cnpj=input ('Digite o CNPJ (Somente Números)..: ')
print (cnpj)

printer = input ('Digite a Porta da Impressora...: ')
print (printer)

config='''configuration

# *************** Geral ******************

# Password para acessar o administrativo
adminPassword=33638205

# Timeout da aplicação em milisegundos
timeout=40000

# Habilita mouse
mouseEnabled=false

# Modo fullscreen
fullscreenModeEnabled=false

# Modelo Impressora (térmica) [diebold | engworks | engworks4i | elgin_bkt6112 | star_tup900 | default]
modelPrinter=elgin_bkt6112

# Porta da impressora para modelos de impressora térmica
portPrint=COM7

# Mensagem padrão para o display do PinPad
displayPinpad=Videosoft

# Captura cliques na Screen Logger API
screenLoggerEnabled=false

# Prefixo para o cupom fiscal que é enviado para as APIs de pagamento, no máximo 7 dígitos, lojapdv
prefixCupomFiscal=1150101

# Habilita pagamento
paymentEnabled=true

# Habilita pagamento mínimo
paymentMinimumEnabled=true

# Habilita botão de desbloqueio de cartão(caso esteja desabilitado, não irá considerar o valor vindo dos CSVs)
cardReleaseEnabled=false

# ************* Database ******************

# URL de conexão do banco de dados
jdbcUrl=jdbc:mysql://localhost:3306/totem_calcard?createDatabaseIfNotExist=true&useSSL=false

# Usuário do banco de dados
jdbcUser=root

# Senha do banco de dados
jdbcPassword=root

# ************* VS AutoPag ****************

# Path do Client de Pagamento com Cartão
vsAutoPagSeCommand=C:\\Program Files\\videosoft\\vs-auto-pag-se\\vs-auto-pag-se-daemon.bat

# ************* VS Conductor ****************

# Path do Client de Pagamento do Módulo Conductor
vsConductorCommand=C:\\Program Files\\videosoft\\vs-conductor\\vs-conductor-daemon.bat

# ***************** Webservice *****************

webserviceContaCartaoService=http://10.19.253.48:30008/ContaCartaoService.asmx?wsdl
webserviceWsCdtConductor=http://10.19.253.48:20008/WS_CDTConductor.asmx?wsdl

apiCalsystemCard=https://totem.calcard.com.br/api/card-engine/v2
apiCalsystemAuth=https://totem.calcard.com.br/oauth
apiCalsystemAccount=https://totem.calcard.com.br/api/account-engine/v4
apiCalsystemRenegotiation=https://totem.calcard.com.br/api/renegotiation-engine/v2
apiCalsystemTotemEngine=https://totem.calcard.com.br/api/totem-engine/v2
apiCalsystemPaymentPCH=https://pch-totem.calcard.com.br/api/totem-app/v2
apiCalsystemCardUser=totem
apiCalsystemCardPassword=d8007891-4207-4cc5-b942-3c24620e33d6

# ***************** Proxy *****************
# Caso a rede não tenha proxy, deixar os campos em branco

# Host
proxyHost=

# Porta
proxyPort=

# Usuário
proxyUser=

# Senha
proxyPassword=
'''


#### prod.properties
# *************** Geral ******************

# Password para acessar o administrativo
adminPassword=33638205

# Prefixo para o cupom fiscal que é enviado para as APIs de pagamento, no máximo 7 dígitos, lojapdv
prefixCupomFiscal=1150101

# ***************** Webservice *****************
prod="""
apiCalsystemCardUser=TOTEM_8205
apiCalsystemCardPassword=8205

apiCalsystemCard=https://pch-totem.calcard.com.br/api/totem-app/v1
apiCalsystemAuth=https://pch-totem.calcard.com.br/api/totem-app/v1
apiCalsystemAccount=https://pch-totem.calcard.com.br/api/totem-app/v1
apiCalsystemRenegotiation=https://pch-totem.calcard.com.br/api/totem-app/v2
apiCalsystemTotemEngine=https://pch-totem.calcard.com.br/api/totem-app/v1
apiCalsystemPaymentPCH=https://pch-totem.calcard.com.br/api/totem-app/v2
"""

config_autopag= """
# ***************** Geral *****************

# Timeout da aplica\u00c3\u00a7\u00c3\u00a3o em segundos
timeout=59

# Modelo Impressora (térmica) [diebold | engworks | engworks4i | elgin_bkt680 | elgin_bkt6112 | bematech_mp_4200_th | star_tup900 | default]
modelPrinter=elgin_bkt6112

# Porta da impressora para modelos de impressora térmica
portPrint=COM7

# Corta o papel ap\u00c3\u00b3s a impress\u00c3\u00a3o do comprovante
cutPaper=true

# Modo fullscreen, caso seja false, ser\u00c3\u00a1 maximizado a janela
fullscreenMode=true

# Habilita/desabilita ponteiro do mouse
mouseEnable=false

# Tempo em segundos para apresenta\u00c3\u00a7\u00c3\u00a3o das mensagens pertinentes ao cliente
messageTime=5

# Tempo em segundos para apresenta\u00e7\u00e3o da \u00faltima mensagem
endMessageTime=5

# Bloquear utiliza\u00c3\u00a7\u00c3\u00a3o do terminal em caso de problemas na impressora
blockTerminal=true

# Mensagem padr\u00c3\u00a3o para o display do PinPad
displayPinpad=Videosoft

# Mostra imagem estatica na tela de inserir o cart\u00c3\u00a3o no pinpad
showImageInsertCard=false

# Mostra imagem estatica na tela de inserir a senha
showImagePassword=false

# ************* Database ******************

# URL de conex\u00c3\u00a3o do banco de dados
jdbcUrl=jdbc:mysql://localhost:3306/vs_auto_pag_se?createDatabaseIfNotExist=true&useSSL=false

# Usu\u00c3\u00a1rio do banco de dados
jdbcUser=root

# Senha do banco de dados
jdbcPassword=root

# ***************** Sitef *****************

# Host
sitefHost=192.168.42.18

# StoreID
sitefStoreId=54009064

# Terminal ID
sitefTerminalId=AA090101

#Par\u00c3\u00a2metros adicionais usados na ConfiguraIntSiTefInterativeEx, exigido para ativar o Cielo Premia
#[VersaoAutomacaoCielo=AAAAAAAACR], onde:
#AAAAAAAA = Nome da Software House da automa\u00c3\u00a7\u00c3\u00a3o (8 bytes)
#C = Deve ser 1 se a automa\u00c3\u00a7\u00c3\u00a3o est\u00c3\u00a1 preparada para tratar o desconto e as transa\u00c3\u00a7\u00c3\u00b5es da Plataforma Promocional e 0 caso contr\u00c3\u00a1rio
#R = Campo reservado, deve ser enviado 0.
#sitefParamAdditional=[VersaoAutomacaoCielo=VIDEOSOF00]

sitefParamAdditional=

# Par\u00c3\u00a2metros adicionais para pagamentos do Sitef
#sitefPaymentParamAdditional={TipoTratamento=4}
sitefPaymentParamAdditional=

# ***************** Proxy *****************
# Caso a rede n\u00c3\u00a3o tenha proxy, deixar os campos em branco

# Host
proxyHost=

# Porta
proxyPort=

# Usu\u00c3\u00a1rio
proxyUser=

# Senha
proxyPassword=
"""
