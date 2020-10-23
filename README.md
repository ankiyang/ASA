# ASA

victim: container_a
legitimate client: container_b
DDoS attacker: container_c

the scenario of attack in container_c need to be execute manually using *hping3*.

## network setup 
> docker network create --subnet 172.168.1.0/24 NetWorkBridge

> docker network connect NetWorkBridge container_a

> docker network connect NetWorkBridge container_b

## steps
> docker build -t container_a .
> docker run --name container_a -d container_a


## check existing containers
> docker ps -a

##
> docker exec -it container_a python src/main.py

##
network bridge:  bridge2

IP_range: 172.19.0.0/16 bridge2

* container_a : 172.19.0.21
* container_b : 172.19.0.22
* container_c : 172.19.0.23
