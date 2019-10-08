#!/usr/bin/env python
# -*- coding: utf-8 -*-
# db_schema - based on dataset and sqlalchemy

from ansible.module_utils.basic import AnsibleModule, iteritems

import requests as rq

def main():
    module = AnsibleModule(
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

    web_host = module.params.get('web_host')
    db_name   = module.params.get('db_name')
    db_user = module.params.get('db_user')
    db_pwd = module.params.get('db_pwd')
    db_host = module.params.get('db_host')
    site_name = module.params.get('site_name')
    site_user = module.params.get('site_user')
    site_pass = module.params.get('site_pass')

    changed = False

    url=["/wp-admin/setup-config.php?step=2","/wp-admin/install.php?step=2"]
    data = [{
      'dbname': db_name,
      'uname': db_user,
      'pwd': db_pwd,
      'dbhost': db_host,
      'prefix': 'wp_',
      'language': 'fr_FR',
      'submit': 'Envoyer'
    },
    {
      'weblog_title': site_name,
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
    while i < 2:
        r = rq.post("http://"+web_host+url[i],data[i])
        print(r.text)
        i=i+1
    changed = True
    module.exit_json(changed=changed)

if __name__ == '__main__':
    main()
