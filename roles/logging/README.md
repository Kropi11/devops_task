# Logging role

## Popis
Úkolem této role je zajištění logování metrik všech kontejnerů a nginxu pomocí python skriptu, běžícího jako daemon. Logovací skript je spuštěn v kontejneru s aplikací Grafana a loguje metriky v intervalu 20 sekund do souboru `metrics.json`. Ten se nachází v adresáři `/var/log/logging_script/`.

## Požadavky
- Ansible
- Spuštěný Grafana kontejner

## Použití
1. Ujistěte se, že v konfiguračním souboru `inventory.ini` jsou správně nastaveny cílové servery.
2. Ujisťěte se, že je spuštěný Grafana kontejner.
3. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/logging_playbook.yml
```
## Struktura role
1. `prepare.yml` - Vytvoří potřebné složky a soubory pro logovací skript na cílovém serveru. Nastaví práva pro spuštění skriptu.
2. `start.yml` - Spustí logovací skript v kontejneru s aplikací Grafana.

## Formát logu
Logovací skript loguje metriky v následujícím formátu:
```json
    {
        "Date-TimeStamp": "2020-08-12 12:32:40",
        "DockerContainerLoad": {
            "container_name": {
                "CpuUsage": 0,
                "MemoryUsage": 0,
                "SwapUsage": 0
            }
        },
        "NginxStatus": {
            "ActiveConnections": 1,
            "ServerAccepts": 6,
            "ServerHandled": 6,
            "ServerRequests": 6,
            "Reading": 0,
            "Writing": 1,
            "Waiting": 0
        },
        "NginxHeaders": [
          ...
        ]
    },
    ...
```