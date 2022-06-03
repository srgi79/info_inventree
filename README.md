# info_inventree
helpers to easyly run Inventree on Raspberry Pi x64

## INSTALATION


## RUN AS A SERVICE IN RPI ##
- Copy **inventree.service** in **/lib/systemd/system** folder
- Reaload systemd:
~~~
sudo systemctl daemon-reload
~~~
- Start service:
~~~
sudo systemctl start inventree.service 
~~~
- If it works, enable the service on boot:
~~~
sudo systemctl enable inventree.service 
~~~
