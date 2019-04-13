
=================================================
|Zeroincombenze| account-financial-reporting 10.0
=================================================

|Maturity| |Build Status| |Coverage Status| |Codecov Status| |license gpl| |Tech Doc| |Help| |Try Me|

.. contents::


Overview / Panoramica
=====================

|en| Financial Reporting

This project aims to deal with modules related to financial reports. You'll 
find modules that print legal and official reports. This includes, among 
others:

* One module based on webkit and totally rewritten by camptocamp, for standard
  financial reports.
* Another based on RML completely improved by Vauxoo.


|it| Stampa finanziarie

Progetto basato sui moduli OCA per la gestione delle stampa finanziare.

Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_bank_statement_line_reconcil | 10.0.1.0.0 | |same|     | OCA Financial Reports                                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_chart_report                 | |halt|     | |halt|     | Print chart of accounts                                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_export_csv                   | |halt|     | |halt|     | Account Export CSV                                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_financial_report             | |halt|     | |halt|     | Common financial reports                                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_financial_report_date_range  | 10.0.1.0.0 | |same|     |  Add Date Range field to the Odoo OE standard addons financial reports wizard.   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_financial_report_horizontal  | 10.0.1.0.0 | |same|     | Accounting Financial Report Horizontal                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_financial_report_qweb        | 10.0.3.0.1 | |same|     | OCA Financial Reports                                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_journal_report_xls           | |halt|     | |halt|     | Financial Journal reports                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_move_line_report_xls         | 10.0.1.0.0 | |same|     | Journal Items Excel export                                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_tax_balance                  | 10.0.1.1.1 | |same|     | Compute tax balances based on date range                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| customer_activity_statement          | 10.0.1.1.0 | |same|     | OCA Financial Reports                                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| customer_outstanding_statement       | 10.0.1.1.0 | |same|     | OCA Financial Reports                                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| mis_builder                          | 10.0.2.0.2 | |no_check| |  Build 'Management Information System' Reports and Dashboards                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| mis_builder_demo                     | |halt|     | |no_check| |  Demo data for the mis_builder module                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+


OCA comparation / Confronto con OCA
-----------------------------------


+-----------------------------------------------------------------+-------------------+-----------------------+--------------------------------+
| Description / Descrizione                                       | Zeroincombenze    | OCA                   | Notes / Note                   |
+-----------------------------------------------------------------+-------------------+-----------------------+--------------------------------+
| Coverage / Copertura test                                       |  |Codecov Status| | |OCA Codecov Status|  | |OCA project|                  |
+-----------------------------------------------------------------+-------------------+-----------------------+--------------------------------+


Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------


* python2.7+
* postgresql 9.2+

Installation / Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /opt/odoo/10.0/account-financial-reporting/                                |
+----------------------------------------------------------------------------+

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository account-financial-reporting -b 10.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 10.0 -vsy -o /opt/odoo/10.0


Upgrade / Aggiornamento
-----------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    odoo_install_repository account-financial-reporting -b 10.0 -O zero -U
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------


|Zeroincombenze| This project is mainly maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/account-financial-reporting/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change this module, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare questo modulo, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

History / Cronologia
--------------------

10.0.3.0.0 (2019-01-09)
~~~~~~~~~~~~~~~~~~~~~~~

* Improve multicompany related usability.
* Improve performance in the General Ledger.
* The reports now display an improved title that includes report name,
  company and currency.


10.0.2.0.0 (2018-11-29)
~~~~~~~~~~~~~~~~~~~~~~~

* The Trial Balance now allows to display the hierarchy of accounts
* In the Trial Balance you can apply a filter by hierarchy levels
* The Trial Balance shows the unaffected earnings account computed as:
  initial balance: sum of past unaffected earnings + P&L result; debit, credit
  and period balance: totals only for the unaffected earnings account.
* In the Journal Ledger the field 'Journal' is now optional


Credits / Titoli di coda
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://wiki.zeroincombenze.org/en/Odoo>`__ è progettata per le esigenze del mercato italiano.


|chat_with_us|


|


Last Update / Ultimo aggiornamento: 2019-04-13

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/account-financial-reporting.svg?branch=10.0
    :target: https://travis-ci.org/zeroincombenze/account-financial-reporting
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/account-financial-reporting/badge.svg?branch=10.0
    :target: https://coveralls.io/github/zeroincombenze/account-financial-reporting?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/account-financial-reporting/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/account-financial-reporting/branch/10.0
    :alt: Codecov
.. |OCA project| image:: Unknown badge-OCA
    :target: https://github.com/OCA/account-financial-reporting/tree/10.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: https://codecov.io/gh/OCA/account-financial-reporting/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/account-financial-reporting/branch/10.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
