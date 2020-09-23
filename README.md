# ASA

## network setup 
docker network create --subnet 172.168.1.0/24 NetWorkBridge
docker network connect NetWorkBridge container_a
docker network connect NetWorkBridge container_b