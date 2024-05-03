# Nginx Role

## Popis
Tato role slouží k nasazení a konfiguraci Nginx serveru na cílovém serveru pomocí Ansible.

Prvně je vytvořena instance Nginx serveru jako webový server pro hostování souborů z lokálního disku. Dále je vytvořena druhá instance Nginx serveru, která je konfigurována jako reverzní cacheující proxy server, využívající první instanci Nginx serveru jako svůj upstream.

Při komunikaci mezi proxy a upstream serverem jsou použity keepalive connections.

Při komunikaci mezi proxy a klientem jsou použity SSL/TLS connections.

## Požadavky
- Ansible
- Docker

## Použití
1. Ujistěte se, že v konfiguračním souboru `inventory.ini` jsou správně nastaveny cílové servery.
2. Spusťte playbook následujícím příkazem:

```bash
ansible-playbook -i inventory.ini playbooks/nginx_playbook.yml
```

## Struktura role
1. `prepare.yml` - Vytvoří potřebné síťové prvky.
2. `setup.yml` - Vytvoří obě instance Nginx serveru a nakonfiguruje je. 
3. `start.yml` - Spustí obě instance Nginx serveru.
4. `config.yml` - Zkopíruje konfigurační soubory pro Nginx servery do kontejnerů.
5. `certificates.yml` - Vytvoří certifikáty pro SSL/TLS spojení mezi reverzní proxy serverem a klientem.

## Konfigurace
V souboru inventory.ini můžete nastavit následující proměnné pro konfiguraci Nginx:

- `nginx_image` - Jméno a verze obrazu Nginx serveru.
- `nginx_file_server_name` - Název první instance Nginx serveru, který slouží jako webový server pro hostování souborů z lokálního disku.
- `nginx_reverse_proxy_name` - Název druhé instance Nginx serveru, který je konfigurován jako reverzní cacheující proxy server a využívá první instanci Nginx serveru jako svůj upstream.
- `certificates_directory` - Adresář obsahující certifikáty pro SSL/TLS spojení.

Pokud není specifikována hodnota pro některou z těchto proměnných, bude použita výchozí hodnota definovaná v `inventory.ini`.

### Konfigurační soubory pro Nginx
Konfigurace Nginx serverů je uložena v adresáři `ansible_project/roles/nginx/files/`. Tento adresář obsahuje konfigurační soubory pro webový server a reverzní proxy server.