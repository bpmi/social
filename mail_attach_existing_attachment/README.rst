===============================
Mail Attach Existing Attachment
===============================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:423e56ee23d174ef9a1f40fb63e30d66ded86a485d11941396aca2c4a500f0c9
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fsocial-lightgray.png?logo=github
    :target: https://github.com/OCA/social/tree/15.0/mail_attach_existing_attachment
    :alt: OCA/social
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/social-15-0/social-15-0-mail_attach_existing_attachment
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/social&target_branch=15.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module was written to add the possibility to add attachments located on
the object by sending it by email with the mail compose message wizard

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

* Adding some attachments on an object by creating a new *Log note*

.. figure:: https://raw.githubusercontent.com/OCA/social/15.0/mail_attach_existing_attachment/static/description/attachment.png
   :alt: Attachment on purchase order

* Then, by sending the object via email, you can select the attachment added earlier

.. figure:: https://raw.githubusercontent.com/OCA/social/15.0/mail_attach_existing_attachment/static/description/ex_mail_compose_message.png
   :alt: Sends the Purchase Order by email

Known issues / Roadmap
======================

* The module only allows the addition of attachments linked to the object.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/social/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/social/issues/new?body=module:%20mail_attach_existing_attachment%0Aversion:%2015.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* ACSONE SA/NV
* Tecnativa

Contributors
~~~~~~~~~~~~

* Adrien Peiffer <adrien.peiffer@acsone.eu>
* `Tecnativa <https://www.tecnativa.com>`_:

  * Sergio Teruel
  * Ernesto Tejeda

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/social <https://github.com/OCA/social/tree/15.0/mail_attach_existing_attachment>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
