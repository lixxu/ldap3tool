#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ldap3
from ldap3 import Server, Connection, SUBTREE

COMMON_FILTERS = dict(display='(displayName={})', name='(sAMAccountName={})',
                      email='(mail={})', phone='(telephoneNumber={})',
                      number='(employeeNumber={})', mobile='(mobile={})',
                      )


class LDAPTool(object):
    def __init__(self, **kwargs):
        self.server = kwargs.get('server')
        self.base_dn = kwargs.get('base_dn')
        self.search_scope = kwargs.get('search_scope') or SUBTREE
        self.retrive_attrs = kwargs.get('retrive_attrs', ldap3.ALL_ATTRIBUTES)
        self.version = kwargs.get('version', 3)

    def connect(self, username, password, auto_bind=True):
        self.conn = Connection(self.server, user=username, password=password,
                               auto_bind=auto_bind)
        return self.conn

    def close(self):
        self.conn.unbind()

    def parse_info(self, attrs={}):
        manager = attrs.get('manager', '').strip().split(',', 1)[0]
        number = attrs.get('employeeNumber', '').strip()
        if not number:
            number = attrs.get('employeeID', '').strip()

        alias_name = attrs.get('extensionAttribute14', '').strip()
        full_name = attrs.get('displayName', '').strip()
        cn = attrs.get('cn', '').strip()
        name = attrs.get('name', '').strip()
        if not alias_name:
            alias_name = full_name or cn or name

        if not full_name:
            full_name = alias_name or name or cn

        return dict(ntname=attrs['sAMAccountName'].strip().lower(),
                    full_name=full_name,
                    alias_name=alias_name,
                    email=attrs.get('mail', '').strip().lower(),
                    manager=manager.split('=')[-1].strip(),
                    title=attrs.get('title', '').strip().upper(),
                    department=attrs.get('department', '').strip().upper(),
                    phone=attrs.get('telephoneNumber', '').strip().lower(),
                    mobile=attrs.get('mobile', '').strip().lower(),
                    number=attrs.get('employeeNumber', '').strip(),
                    )

    def search_by(self, filter_value, **kwargs):
        limit = kwargs.pop('limit', None)
        if 'paged_size' in kwargs:
            limit = kwargs.pop('paged_size')

        as_raw = kwargs.pop('as_raw', False)
        self.conn.search(search_base=self.base_dn,
                         search_filter=filter_value,
                         search_scope=self.search_scope,
                         attributes=self.retrive_attrs,
                         paged_size=limit, **kwargs)
        results = []
        for entry in self.conn.response:
            if 'attributes' in entry:
                if as_raw:
                    results.append(entry['attributes'])
                else:
                    results.append(self.parse_info(entry['attributes']))

        return results

    def search_name(self, name, limit=1, **kwargs):
        return self.search_by(COMMON_FILTERS['name'].format(name), limit=limit,
                              **kwargs)

    def search_email(self, email, limit=1, **kwargs):
        return self.search_by(COMMON_FILTERS['email'].format(email),
                              limit=limit, **kwargs)

    def search_mail(self, email, limit=1, **kwargs):
        return self.search_email(email, limit, **kwargs)

    def search_phone(self, phone, limit=1, **kwargs):
        return self.search_by(COMMON_FILTERS['phone'].format(phone),
                              limit=limit, **kwargs)

    def search_mobile(self, mobile, limit=1, **kwargs):
        return self.search_by(COMMON_FILTERS['mobile'].format(mobile),
                              limit=limit, **kwargs)

    def search_number(self, number, limit=1, **kwargs):
        return self.search_by(COMMON_FILTERS['number'].format(number),
                              limit=limit, **kwargs)

    def search_display(self, display_name, limit=1, **kwargs):
        return self.search_by(COMMON_FILTERS['display'].format(display_name),
                              limit=limit, **kwargs)
