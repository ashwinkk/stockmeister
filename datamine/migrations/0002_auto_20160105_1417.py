# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='AfterHoursChangeRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='Ask',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='AskRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='AverageDailyVolume',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='Bid',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='BidRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='ChangeFromFiftydayMovingAverage',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='ChangeFromYearHigh',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='ChangeFromYearLow',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='ChangePercentRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='ChangeRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='ChangeinPercent',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='Currency',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='DaysHigh',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='DaysLow',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='DaysRange',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='DaysRangeRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='DaysValueChange',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='DaysValueChangeRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='DividendShare',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='EarningsShare',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='FiftydayMovingAverage',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='HoldingsGainRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='LastTradeDate',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='LastTradeRealtimeWithTime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='LastTradeTime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='LastTradeWithTime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='MarketCapRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='MarketCapitalization',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='MoreInfo',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='Open',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='OrderBookRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PERatio',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PERatioRealtime',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PercebtChangeFromYearHigh',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PercentChangeFromFiftydayMovingAverage',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PercentChangeFromYearLow',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PreviousClose',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='PricePaid',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='StockExchange',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='TradeDate',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='Volume',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='YearHigh',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='YearLow',
        ),
        migrations.RemoveField(
            model_name='stocks_intraday',
            name='YearRange',
        ),
    ]