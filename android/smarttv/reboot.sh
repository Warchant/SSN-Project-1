ip=$1
[ x${ip} == x ] && exit 1

echo 'POST /smp_4_ HTTP/1.1
Host: ' $ip '
SOAPAction: "urn:samsung.com:service:MainTVAgent2:1#SetMainTVChannel"
Accept-Language: en-us;q=1, en;q=0.5
Accept-Encoding: gzip
Content-Type: text/xml; charset="utf-8"
User-Agent: gupnp-universal-cp GUPnP/0.20.18 DLNADOC/1.50
Connection: Keep-Alive
Content-Length: 348

<?xml version="1.0"?><s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:SetMainTVChannel xmlns:u="urn:samsung.com:service:MainTVAgent2:1"><Channel></Channel><SatelliteID>0</SatelliteID><ChannelListType>0</ChannelListType></u:SetMainTVChannel></s:Body></s:Envelope>' | nc $ip 7676
