# Generated by Django 2.1.1 on 2018-09-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denizen', '0002_auto_20180915_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denizen',
            name='hood',
            field=models.CharField(blank=True, choices=[('בבלי צמרות איילון והצפון החדש', 'בבלי צמרות איילון והצפון החדש'), ('הכרם ונווה צדק', 'הכרם ונווה צדק'), ('הצפון הישן (צפוני ודרומי)', 'הצפון הישן (צפוני ודרומי)'), ('התקווה ודרום מזרח העיר', 'התקווה ודרום מזרח העיר'), ('יד אליהו', 'יד אליהו'), ('יפו', 'יפו'), ('לב העיר', 'לב העיר'), ('מעוז אביב והדר יוסף', 'מעוז אביב והדר יוסף'), ("נאות אפקה א' ו-ב'", "נאות אפקה א' ו-ב'"), ('נווה אביבים וסביבתה ורמת אביב', 'נווה אביבים וסביבתה ורמת אביב'), ('נחלת יצחק בצרון ורמת ישראל', 'נחלת יצחק בצרון ורמת ישראל'), ("עג'מי וגבעת עלייה", "עג'מי וגבעת עלייה"), ('פלורנטין ונווה שאנן', 'פלורנטין ונווה שאנן'), ('צהלה והמשתלה', 'צהלה והמשתלה'), ('צפון חדש - כיכר המדינה והדרומי', 'צפון חדש - כיכר המדינה והדרומי'), ('צפון יפו', 'צפון יפו'), ('צפון מערביות', 'צפון מערביות'), ('רביבים שיכון דן ונווה דן', 'רביבים שיכון דן ונווה דן'), ("רמת אביב ג' ואפקה", "רמת אביב ג' ואפקה"), ('רמת החייל ונווה שרת', 'רמת החייל ונווה שרת'), ('שפירא קרית שלום וסביבתה', 'שפירא קרית שלום וסביבתה'), ('תל ברוך ותל ברוך צפון', 'תל ברוך ותל ברוך צפון')], max_length=32, verbose_name='Neighborhood'),
        ),
    ]