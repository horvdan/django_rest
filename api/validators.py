from django.core.validators import RegexValidator

currency_code_validator = RegexValidator(regex='^[A-Z]{3}$', message='Must be 3 uppercase character', code='nomatch')
