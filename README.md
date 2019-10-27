# Wordpress_Ansible_Auto
Ce rôle permet d'installer wordpress automatiquement sur des serveurs RedHat/CentOS ou Debian/Ubuntu.
## Prérequis
Pour que le rôle Wordpress installe automatiquement Wordpress depuis un environnement fraîchement installé plusieurs rôles sont requis, ces rôles se trouvent dans le répertoire`roles`.
- [ansible-role-apache](https://github.com/geerlingguy/ansible-role-apache) 
- [ansible-role-php](https://github.com/geerlingguy/ansible-role-php) 
- [ansible-role-apache-php-fpm](https://github.com/geerlingguy/ansible-role-apache-php-fpm) 
- [ansible-role-mysql](https://github.com/geerlingguy/ansible-role-mysql) 
- ansible-role-pip

## Variables
### Apache
Les variables sont récupérées dans`vars/Apache.yml`:
> Apache
- `documentroot` : contient le chemin d'installation de Wordpress.

### Mysql
Les variables sont récupérées dans`vars/Mysql.yml`:
> Base de donnés:
- `name`  : contient le nom de la base de données.

> Utilisateurs:
- `password` : contient le mot de passe de l'utilisateur de la base de données.

### Wordpress
Les variables sont récupérées dans`vars/Mysql.yml`:
> Wordpress:
- `site_user` : contient le nom de l'utilisateur Wordpress.
- `site_pass` : contient le mot de passe de l'utilisateur Wordpress.


## Exemple Playbook Wordpress_install

 `Playbook.yml`:
 
    - hosts: wordpress
      remote_user: user
      become: yes
      vars_files:
         - vars/Apache.yml
         - vars/Mysql.yml
         - vars/Wordpress.yml
      roles:
         - wordpress
         
 `host.yml`:

    [wordpress]
	<ip-web-host> site_name=nomdusite db_host=<ip-bdd-host>
## License
MIT / BSD

Les rôles ci dessous appartiennent à [Jeff Gerling :](https://github.com/geerlingguy)
- [ansible-role-apache](https://github.com/geerlingguy/ansible-role-apache) 
- [ansible-role-php](https://github.com/geerlingguy/ansible-role-php) 
- [ansible-role-apache-php-fpm](https://github.com/geerlingguy/ansible-role-apache-php-fpm) 
- [ansible-role-mysql](https://github.com/geerlingguy/ansible-role-mysql) 
