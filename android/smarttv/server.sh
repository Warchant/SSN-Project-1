(
    cat <<EOF
HTTP/1.1 200 OK
x-amz-id-2: 9Nugr1iLITqHHJXzBeCTLimys5TeanKwuEre92HoHb3+xZaLgM/SR/pPVnd1nrsaTG9BqzOpFjU=
x-amz-request-id: 5F706284E2A18893
Last-Modified: Fri, 17 Jun 2016 05:08:12 GMT
ETag: "7078cd7e79632ef2556b4f1ba696599c-8"
Accept-Ranges: bytes
Content-Type: binary/octet-stream
Content-Length: 99953714944
Server: AmazonS3
Expires: Fri, 02 Dec 2016 19:08:11 GMT
Cache-Control: max-age=0, no-cache
Pragma: no-cache
Date: Fri, 02 Dec 2016 19:08:11 GMT
Connection: keep-alive

EOF
dd if=/dev/urandom bs=1M count=2048
) | sudo nc -lp 80
