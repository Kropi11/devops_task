# Host preparation Role

## Popis
Role `host_preparation` slouží k přípravě cílového serveru pro běh dalších rolí. Instaluje potřebné balíčky a nastavuje základní konfiguraci serveru.

## Požadavky
- Ansible

## Použití
1. Upravte soubor `inventory.ini`, aby obsahoval správně nastavené cílové servery
2. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/host_preparation_playbook.yml
```

## Struktura role
1. `system_packages.yml` - Instalace potřebných balíčků pro běh všech rolí
2. `docker.yml` - Instalace Dockeru