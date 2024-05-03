# Grafana Role

## Popis

Tato role slouží k nasazení a konfiguraci Grafany pro monitorování infrastruktury pomocí metrik sbíraných pomocí Prometheusu a příslušných exportérů.

## Požadavky

- Ansible
- Docker (pokud není již nainstalován)
- Prometheus a odpovídající exportéry pro sběr metrik z ostatních VM/kontejnerů

## Použití

1. Upravte soubor `inventory.ini`, aby obsahoval správně nastavené cílové servery
2. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/grafana_playbook.yml
```
## Struktura role
1. `prepare.yml` - Vytváří potřebné síťové prvky a zabezpečuje, že je Docker image správně zbuildován.
2. `setup.yml` - Vytváří kontejner s potřebnými nastaveními pro běh Grafany.
3. `start.yml` - Spouští kontejner s Grafanou.
4. `dashboard.yml` - Vytváří datasource pro prometheus a stahuje a importuje dashboard pro node_exporter, aby bylo možné zobrazit data v Grafana dashboardu.

## Konfigurace
V souboru `inventory.ini` je možné nastavit následující proměnné pro konfiguraci Grafany:

- `grafana_name` - Název kontejneru, ve kterém bude Grafana spuštěna.
- `grafana_image` - Jméno a verze obrazu, který bude použit pro kontejner s Grafanou.
- `grafana_restart_policy` - Politika restartování kontejneru v případě selhání.
- `grafana_env_admin_user` - Uživatelské jméno pro přihlášení do Grafany jako administrátor.
- `grafana_env_admin_password` - Heslo pro přihlášení do Grafany jako administrátor.
- `grafana_env_anonymous_enabled` - Povolení nebo zakázání anonymního přístupu k Grafaně.
- `grafana_port` - Port, na kterém bude Grafana dostupná.

Pokud není specifikována hodnota pro některou z těchto proměnných, bude použita výchozí hodnota definovaná v `inventory.ini`.

### Dockerfile
V adresáři `ansible_project/roles/grafana/files` naleznete `Dockerfile`, který je založen na Debianu a obsahuje konfiguraci Grafany a dalších komponent potřebných pro běh kontejneru a python skriptu definovaného v `log_playbook.yml`.