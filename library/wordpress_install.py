#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auteur alwarel (Antoine Vn)
# Script d'automatisation d'installation de Wordpress

from ansible.module_utils.basic import AnsibleModule, iteritems # Importation des librairie d'Ansible

import requests as rq # Importation de la la librairie request

def main():
    module = AnsibleModule( #récupération des variables d'Ansible
        argument_spec=dict(
            web_host = dict(required=True, type='str'),
            db_name   = dict(required=True, type='str'),
            db_user   = dict(required=True, type='str'),
            db_pwd   = dict(required=True, type='str'),
            db_host  = dict(required=True, type='str'),
            site_name   = dict(required=True, type='str'),
            site_user   = dict(required=True, type='str'),
            site_pass   = dict(required=True, type='str')
            ))

    web_host = module.params.get('web_host') # Définition de la variable Web_host = IP du serveur Web
    db_name   = module.params.get('db_name') # Définition de la variable db_name = Nom de la base de données
    db_user = module.params.get('db_user') # Définition de la variable db_user = L'utilisateur pour se connecter à la base de données
    db_pwd = module.params.get('db_pwd') # Définition de la variable db_pwd = Le mot de passe pour se connecter à la base de données
    db_host = module.params.get('db_host') # Définition de la variable db_host = IP du serveur de base de données
    site_name = module.params.get('site_name') # Définition de la variable site_name = Nom du site Wordpress
    site_user = module.params.get('site_user') # Définition de la variable site_user = Nom de l'utilisateur pour se connecter à Wordpress
    site_pass = module.params.get('site_pass') # Définition de la variable site_pass = Mot de passe pour se connecter à Wordpress

    changed = False

    url=["/wp-admin/setup-config.php?step=2","/wp-admin/install.php?step=2"] # Définition des urls où sont envoyés les formulaire de Wordpress
    data = [{ # Définition du dictionnaire contenant les données envoyés lors du 1er formulaire
      'dbname': db_name,
      'uname': db_user,
      'pwd': db_pwd,
      'dbhost': db_host,
      'prefix': 'wp_',
      'language': 'fr_FR',
      'submit': 'Envoyer'
    },
    {
      'weblog_title': site_name, # Définition du dictionnaire contenant les données envoyés lors du 2eme formulaire
      'user_name': site_user,
      'admin_password': site_pass,
      'pass1-text': site_pass,
      'admin_password2': site_pass,
      'pw_weak': 'on',
      'admin_email': 'email@mail.fr',
      'language': 'fr_FR',
      'Submit': 'Installer WordPress'
    }]
    i=0
    while i < 2: # Boucle qui se répète 2 fois
        r = rq.post("http://"+web_host+url[i],data[i]) # Envoi de la requête
        print(r.text)
        i=i+1
    changed = True
    module.exit_json(changed=changed)

if __name__ == '__main__':
    main()
