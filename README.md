# apoio-piratas

`PEQUENO PROJETO DE APOIO AO PARTIDO PIRATA`

Instruções sobre como instalar as dependências e rodar o site.

O site depende de Django, instale usando pip (pip3 pois preferimos Python 3).
```
$ sudo pip3 install django
```

Se precisar instale o pip primeiro, use o instalador de pacotes da distribuição linux de sua escolha.

Tire um git clone do repositório:
```
$ git clone https://github.com/piratas/apoio-piratas.git
```

Para rodar em modo desenvolvedor, chame de dentro do diretório `apoio/` o seguinte comando:
```
$ python3 manage.py runserver
```

=======

# Rodando com Docker ou Docker-compose

Para instalar o docker siga:

Mac: https://docs.docker.com/mac/
Linux: https://docs.docker.com/linux/
Windows: https://docs.docker.com/windows/


## Docker compose

```
# docker-compose up -d
```


Acesse via:

Linux:http://127.0.0.1

Mac ou Windows: http://192.168.99.100 (caso não funcione, pegue o IP da docker-machine com:  $docker-machine ip

Para desligar o container
```
# docker-compose stop -d
```

Para visualizar os logs usando docker
Primeiro descubra o nome ou id do container
```
# docker ps 
```

Depois analise os logs
```
# docker logs -f nome ou id
```

Para analisar os logs no host 
```
journalctl CONTAINER_NAME=nome
```

Para mais informações sobre como foi configurado o log vejam [aqui](https://docs.docker.com/engine/admin/logging/journald/)
