[![Build Status](https://travis-ci.org/zeroincombenze/account-financial-reporting.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/account-financial-reporting)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/account-financial-reporting/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/account-financial-reporting?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/account-financial-reporting/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/account-financial-reporting/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/account-financial-reporting/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

    :alt: License
=================

Journal Items Excel Export

This module extends the functionality of the journal items 
('account.move.line') list view and allow you to export the selected lines.

Installation
------------


To install this module, you need also the **report_xls**
module located in:

https://github.com/OCA/reporting-engine

Configuration
-------------

Usage
-----

=====

To use this module, you need to:

* go to the list view of the journal items
* select the lines you wish to export
* click on the button on top to export

The Excel export can be tailored to your exact needs via the following methods
of the 'account.move.line' object:

*  **_report_xls_fields**

   Add/drop columns or change order from the list of columns that are defined
   in the Excel template.

   The following fields are defined in the Excel template:

     move, name, date, journal, period, partner, account,
     date_maturity, debit, credit, balance,
     reconcile, reconcile_partial, analytic_account,
     ref, partner_ref, tax_code, tax_amount, amount_residual,
     amount_currency, currency_name, company_currency,
     amount_residual_currency, product, product_ref', product_uom, quantity,
     statement, invoice, narration, blocked

* **_report_xls_template**

  Change/extend the Excel template.

Known issues / Roadmap
----------------------

Bug Tracker
-----------

Credits
-------


Author
* Luc De Meyer, Noviat <info@noviat.com>

[![Odoo Italia Associazione]]

### Contributors

* Guillaume Auger <guillaume.auger@savoirfairelinux.com>

Icon
----
* https://openclipart.org/detail/38353/58294main-The.Brain.in.Space-page-91-spreadsheet-by-rejon

### Funders

### Maintainer

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
