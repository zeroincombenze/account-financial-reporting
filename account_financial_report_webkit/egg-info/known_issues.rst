In order to run properly this module makes sure you have installed the
library `wkhtmltopdf` for the pdf rendering (the library path must be
set in a System Parameter `webkit_path`).

Initial balances in these reports are based either on opening entry
posted in the opening period or computed on the fly. So make sure
that your past accounting opening entries are in an opening period.
Initials balances are not computed when using the Date filter (since a
date can be outside its logical period and the initial balance could
be different when computed by data or by initial balance for the
period). The opening period is assumed to be the Jan. 1st of the year
with an opening flag and the first period of the year must start also
on Jan 1st.

Totals for amounts in currencies are effective if the partner belongs to
an account with a secondary currency.

HTML headers and footers are deactivated for these reports because of
an issue in wkhtmltopdf
(http://code.google.com/p/wkhtmltopdf/issues/detail?id=656) Instead,
the header and footer are created as text with arguments passed to
wkhtmltopdf. The texts are defined inside the report classes.
