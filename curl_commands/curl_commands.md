#### SOAP API (xml input and output)
curl --header "Content-Type: text/xml;charset=UTF-8" --header "SOAPAction: (methodofservice eg:post)" --data @request.xml "http://fqdn:port/xx/WSDL/public/xx/(webservice)"

#### REST API (xml input and output)
curl -u (user):(password) -X "(methodofservice eg:POST)" -H "X-Requested-With: curl" -H "Content-Type: text/xml"  --data-binary @file.xml "(url)"