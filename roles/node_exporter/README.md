# Node Exporter Role

## Popis

Tato role slouží k instalaci a konfiguraci Node Exporteru na cílovém serveru pomocí Ansible.

Nejprve je vytvořen kontejner s Node Exporterem a následně je spuštěn s nastavenými proměnnými prostředí.

## Požadavky

- Ansible
- Docker

## Použití

1. Ujistěte se, že v konfiguračním souboru `inventory.ini` jsou správně nastaveny cílové servery.
2. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/node_exporter_playbook.yml
```

## Struktura role
1. `prepare.yml` - Vytvoří potřebné síťové prvky.
2. `setup.yml` - Vytvoří kontejner s Node Exporterem.
3. `start.yml` - Spustí kontejner s Node Exporterem.

## Konfigurace

V souboru `inventory.ini` je možné nastavit následující proměnné pro konfiguraci Node Exporteru:

- `node_exporter_name` - Název kontejneru, ve kterém bude Node Exporter spuštěn.
- `node_exporter_image` - Jméno a verze obrazu, který bude použit pro kontejner s Node Exporterem.
- `node_exporter_restart_policy` - Politika restartování kontejneru v případě selhání.
- `node_exporter_env_timezone` - Časová zóna pro Node Exporter.
- `node_exporter_port` - Port, na kterém bude Node Exporter dostupný.

Pokud není specifikována hodnota pro některou z těchto proměnných, bude použita výchozí hodnota definovaná v `inventory.ini`.