#!/usr/bin/env python3
from datetime import datetime, date
import dev_aberto
import gettext
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number


gettext.install('cli', localedir='locale') 


if __name__ == '__main__':
    today = date.today()
    print(format_date(today, format='full'))

    commit_date, commit_name = dev_aberto.hello()
    date_str  = datetime.strptime(commit_date, "%Y-%m-%dT%H:%M:%SZ")
    print(_('Last commit made in:'), format_datetime(date_str), _('by'), commit_name)

    name = input(_('Input your name: '))
    print(_('Hello {}'.format(name)))


