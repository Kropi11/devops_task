# Zookeeper Role

## Popis
Tato role slouží k instalaci a konfiguraci Zookeeperu na cílovém serveru pomocí Ansible.

Nejprve je vytvořen kontejner s Zookeeperem a následně je spuštěn s nastavenými proměnnými prostředí tak, aby odolal výpadkům.

## Požadavky
- Ansible
- Docker

## Použití
1. Ujistěte se, že v konfiguračním souboru `inventory.ini` jsou správně nastaveny cílové servery.
2. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/zookeeper_playbook.yml
 ```

## Struktura role
1. `prepare.yml` - Vytvoří potřebné síťové prvky.
2. `setup.yml` - Vytvoří kontejner s Zookeeperem.
3. `start.yml` - Spustí kontejner s Zookeeperem.

## Konfigurace
V souboru `inventory.ini` můžete nastavit následující proměnné pro konfiguraci Zookeeperu:

- `zookeeper_name` - Název kontejneru, ve kterém bude Zookeeper spuštěn.
- `zookeeper_image` - Jméno a verze obrazu, který bude použit pro kontejner s Zookeeperem.
- `zookeeper_restart_policy` - Politika restartování kontejneru v případě selhání.
- `zookeeper_port` - Port, na kterém bude Zookeeper dostupný.

Pokud není specifikována hodnota pro některou z těchto proměnných, bude použita výchozí hodnota definovaná v `inventory.ini`.