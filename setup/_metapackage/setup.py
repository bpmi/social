import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-social",
    description="Meta package for oca-social Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-base_search_mail_content>=15.0dev,<15.1dev',
        'odoo-addon-base_user_signature>=15.0dev,<15.1dev',
        'odoo-addon-email_template_qweb>=15.0dev,<15.1dev',
        'odoo-addon-fetchmail_mail_activity_team_activity>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_board>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_creator>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_done>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_partner>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_plan>=15.0dev,<15.1dev',
        'odoo-addon-mail_activity_team>=15.0dev,<15.1dev',
        'odoo-addon-mail_attach_existing_attachment>=15.0dev,<15.1dev',
        'odoo-addon-mail_autosubscribe>=15.0dev,<15.1dev',
        'odoo-addon-mail_composer_cc_bcc>=15.0dev,<15.1dev',
        'odoo-addon-mail_debrand>=15.0dev,<15.1dev',
        'odoo-addon-mail_drop_target>=15.0dev,<15.1dev',
        'odoo-addon-mail_improved_tracking_value>=15.0dev,<15.1dev',
        'odoo-addon-mail_layout_force>=15.0dev,<15.1dev',
        'odoo-addon-mail_layout_preview>=15.0dev,<15.1dev',
        'odoo-addon-mail_no_user_assign_notification>=15.0dev,<15.1dev',
        'odoo-addon-mail_notification_custom_subject>=15.0dev,<15.1dev',
        'odoo-addon-mail_optional_autofollow>=15.0dev,<15.1dev',
        'odoo-addon-mail_optional_follower_notification>=15.0dev,<15.1dev',
        'odoo-addon-mail_outbound_static>=15.0dev,<15.1dev',
        'odoo-addon-mail_parent_recipient>=15.0dev,<15.1dev',
        'odoo-addon-mail_partner_opt_out>=15.0dev,<15.1dev',
        'odoo-addon-mail_post_defer>=15.0dev,<15.1dev',
        'odoo-addon-mail_preview_audio>=15.0dev,<15.1dev',
        'odoo-addon-mail_preview_base>=15.0dev,<15.1dev',
        'odoo-addon-mail_quoted_reply>=15.0dev,<15.1dev',
        'odoo-addon-mail_restrict_follower_selection>=15.0dev,<15.1dev',
        'odoo-addon-mail_send_copy>=15.0dev,<15.1dev',
        'odoo-addon-mail_show_follower>=15.0dev,<15.1dev',
        'odoo-addon-mail_tracking>=15.0dev,<15.1dev',
        'odoo-addon-mail_tracking_mailgun>=15.0dev,<15.1dev',
        'odoo-addon-mail_tracking_mass_mailing>=15.0dev,<15.1dev',
        'odoo-addon-mass_mailing_custom_unsubscribe>=15.0dev,<15.1dev',
        'odoo-addon-mass_mailing_custom_unsubscribe_event>=15.0dev,<15.1dev',
        'odoo-addon-mass_mailing_event_registration_exclude>=15.0dev,<15.1dev',
        'odoo-addon-mass_mailing_list_dynamic>=15.0dev,<15.1dev',
        'odoo-addon-mass_mailing_partner>=15.0dev,<15.1dev',
        'odoo-addon-mass_mailing_resend>=15.0dev,<15.1dev',
        'odoo-addon-microsoft_outlook_single_tenant>=15.0dev,<15.1dev',
        'odoo-addon-outgoing_email_by_model>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
