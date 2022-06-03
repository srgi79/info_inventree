# info_inventree
helpers to easyly run Inventree on Raspberry Pi x64

## INSTALATION


## RUN AS A SERVICE IN RPI ##
- Copy **inventree.service** in **/lib/systemd/system** folder
- Copy **inventree_worker.service** in **/lib/systemd/system** folder
- Reaload systemd:
~~~
sudo systemctl daemon-reload
~~~
- Start services:
~~~
sudo systemctl start inventree.service 
~~~
~~~
sudo systemctl start inventree_worker.service 
~~~
- If it works, enable the services on boot:
~~~
sudo systemctl enable inventree.service 
~~~
~~~
sudo systemctl enable inventree_worker.service 
~~~
