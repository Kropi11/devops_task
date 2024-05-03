# Kafka Role

## Účel
Tato role slouží k nasazení a konfiguraci distribuovaného clusteru Apache Kafka, který odolává výpadku 2 instancí služby.

## Požadavky
- Ansible
- Zookeeper
- Docker (pokud není již nainstalován)

## Použití
1. Upravte soubor `inventory.ini`, aby obsahoval správně nastavené cílové servery.
2. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/kafka_playbook.yml
```

## Struktura role
1. `prepare.yml`- Vytváří potřebné síťové prvky.
2. `setup.yml`- Vytváří kontejner s Apache Kafka a konfiguruje ho.
3. `start.yml`- Spouští kontejner s Apache Kafka.

## Konfigurace
V souboru inventory.ini je možné nastavit následující proměnné pro konfiguraci Apache Kafka:

- `kafka_name` - Název kontejneru, ve kterém bude Apache Kafka spuštěna.
- `kafka_image` - Jméno a verze obrazu, který bude použit pro kontejner s Apache Kafka.
- `kafka_restart_policy` - Politika restartování kontejneru v případě selhání.
- `kafka_port` - Vnější port, na kterém bude Apache Kafka dostupná.
- `kafka_exposed_port` - Interní port pro komunikaci mezi Kafka instancemi.
- `kafka_zookeeper_port` - Port, na kterém bude Zookeeper dostupný pro Apache Kafka.
- `kafka_replication_factor` - Počet replikací zpráv pro odolnost vůči výpadkům.
- `kafka_advertised_listeners` - Nastavení posluchačů Kafka pro komunikaci mezi různými instancemi.
- `kafka_listener_security_protocol_map` - Mapování bezpečnostních protokolů pro posluchače Kafka.
- `kafka_listeners` - Konfigurace posluchačů Kafka pro různé typy komunikace.
- `kafka_inter_broker_listener_name` - Název posluchače pro komunikaci mezi různými instancemi Kafka.
- `kafka_create_topics` - Nastavení výchozích témat Kafka.

Pokud není specifikována hodnota pro některou z těchto proměnných, bude použita výchozí hodnota definovaná v `inventory.ini`.