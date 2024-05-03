# Prometheus Role

## Popis

Tato role slouží k instalaci a konfiguraci serveru Prometheus na cílovém serveru pomocí Ansible.

Nejprve je vytvořen kontejner s Prometheusem a následně je spuštěn s nastavenými proměnnými prostředí.

## Požadavky

- Ansible
- Docker

## Použití

1. Ujistěte se, že v konfiguračním souboru `inventory.ini` jsou správně nastaveny cílové servery.
2. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/prometheus_playbook.yml
```

## Struktura role
1. `prepare.yml` - Vytvoří potřebné síťové prvky.
2. `setup.yml` - Vytvoří kontejner s Prometheusem.
3. `start.yml` - Spustí kontejner s Prometheusem.

## Konfigurace

V souboru `inventory.ini` je možné nastavit následující proměnné pro konfiguraci serveru Prometheus:

- `prometheus_name` - Název kontejneru, ve kterém bude Prometheus spuštěn.
- `prometheus_image` - Jméno a verze obrazu, který bude použit pro kontejner s Prometheus.
- `prometheus_restart_policy` - Politika restartování kontejneru v případě selhání.
- `prometheus_env_timezone` - Časová zóna pro Prometheus.
- `prometheus_volumes_config` - Cesta k adresáři s konfiguračními soubory pro Prometheus.
- `prometheus_port` - Port, na kterém bude Prometheus dostupný.

Pokud není specifikována hodnota pro některou z těchto proměnných, bude použita výchozí hodnota definovaná v `inventory.ini`.

### Konfigurační soubor pro Prometheus
Konfigurační soubor pro Prometheus (`prometheus.yml`) je umístěn v adresáři `ansible_project/roles/prometheus/files/`. Zde lze upravit různé nastavení, jako jsou cíle pro sběr metrik, konfigurace služeb a další.