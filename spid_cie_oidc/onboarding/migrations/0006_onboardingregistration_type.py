# Generated by Django 4.0.2 on 2022-03-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_onboarding', '0005_alter_onboardingregistration_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='onboardingregistration',
            name='type',
            field=models.CharField(blank=True, choices=[('federation_entity', 'federation_entity'), ('openid_relying_party', 'openid_relying_party'), ('openid_provider', 'openid_provider'), ('oauth_resource', 'oauth_resource')], default='openid_relying_party', help_text='OpenID Connect Federation entity type', max_length=33),
        ),
    ]