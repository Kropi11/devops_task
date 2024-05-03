# CDN77 DevOps Task

Tento projekt je součástí úlohy CDN DevOps, která si klade za cíl vytvořit virtuální infrastrukturu pomocí Ansible playbooků a dalších nástrojů pro automatizaci. Infrastruktura zahrnuje několik služeb, včetně monitoringu pomocí Prometheusu a Grafany, Nginx jako reverzní proxy, a distribuovaný systém jako Kafka.

## Obsah

- [Požadavky](#požadavky)
- [Úkoly](#úkoly)
  - [Monitoring](#monitoring)
  - [Nginx](#nginx)
  - [Distribuovaný systém](#distribuovaný-systém)
  - [Vlastní skript/program](#vlastní-skriptprogram)
- [Playbooky](#playbooky)
  - [Grafana Playbook](./roles/grafana/README.md)
  - [Host Preparation Playbook](./roles/host_preparation/README.md)
  - [Kafka Playbook](./roles/kafka/README.md)
  - [Log Playbook](./roles/logging/README.md)
  - [Nginx Playbook](./roles/nginx/README.md)
  - [Node Exporter Playbook](./roles/node_exporter/README.md)
  - [Prometheus Playbook](./roles/prometheus/README.md)
  - [Zookeeper Playbook](./roles/zookeeper/README.md)

## Požadavky

Pro spuštění playbooků je potřeba mít nainstalovaný Ansible a SSH přístup k cílovým serverům. Pro instalaci Ansible na Ubuntu lze použít následující příkazy:

```bash
sudo apt-get update
sudo apt-get install ansible
```

## Úkoly
### Monitoring
Monitoring se skládá ze tří hlavních komponent:
- Prometheus - sběr metrik
- Node Exporter - sběr metrik z hostitelského systému
- Grafana - vizualizace metrik

Všechny tři komponenty jsou nasazeny jako kontejnery pomocí Dockeru. Grafana obsahuje dashboardy pro zobrazení metrik z Prometheusu a Node Exporteru.

Pro spuštění monitoringu je potřeba dodržet následující postup:
1. Spustit playbook pro Node Exporter
2. Spustit playbook pro Prometheus
3. Spustit playbook pro Grafanu

```bash
ansible-playbook -i inventory.ini playbooks/node_exporter_playbook.yml playbooks/prometheus_playbook.yml playbooks/grafana_playbook.yml 
```

### Nginx
Nginx je nasazen ve 2 instancích, jako reverzní proxy a webový server. Webový server slouží k hostování souborů z lokálního disku. Reverzní proxy server je konfigurován tak, aby používal webový server jako svůj upstream.

Pro spuštění Nginx je zapotřebí pustit následující playbook:

```bash
ansible-playbook -i inventory.ini playbooks/nginx_playbook.yml
```

### Distribuovaný systém
Jako distribuovaný systém je použit Kafka. Kafka je nasazena ve 4 instancích, kde tři instance slouží jako Zookeeper a jedna instance jako Kafka broker. Tím je zajištěna dostupnost a odolnost systému. 

Pro spuštění Kafka je potřeba pustit následující playbooky:

```bash
ansible-playbook -i inventory.ini playbooks/zookeeper_playbook.yml playbooks/kafka_playbook.yml
```

### Vlastní skript/program
V rámci úkolu je vytvořen python skript, který bude logovat metriky z kontejnerů a Nginx serveru. Skript je spuštěn v kontejneru s aplikací Grafana a bude logovat metriky do souboru `metrics.json` v adresáři `/var/log/logging_script/`.

Pro spuštění skriptu je potřeba pustit následující playbook:

```bash
ansible-playbook -i inventory.ini playbooks/logging_playbook.yml
```

## Playbooky
- [Grafana Playbook](./roles/grafana/README.md)
- [Host Preparation Playbook](./roles/host_preparation/README.md)
- [Kafka Playbook](./roles/kafka/README.md)
- [Logging Playbook](./roles/logging/README.md)
- [Nginx Playbook](./roles/nginx/README.md)
- [Node Exporter Playbook](./roles/node_exporter/README.md)
- [Prometheus Playbook](./roles/prometheus/README.md)
- [Zookeeper Playbook](./roles/zookeeper/README.md)

Pro spuštění všech playbooků najednou lze použít následující příkaz:

```bash
ansible-playbook -i inventory.ini playbooks/host_preparation_playbook.yml playbooks/node_exporter_playbook.yml playbooks/prometheus_playbook.yml playbooks/grafana_playbook.yml playbooks/nginx_playbook.yml playbooks/zookeeper_playbook.yml playbooks/kafka_playbook.yml playbooks/logging_playbook.yml
```