# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks_interday',
            fields=[
                ('Symbol', models.CharField(max_length=20, serialize=False, primary_key=True, blank=True)),
                ('Volume', models.CharField(max_length=20, null=True, blank=True)),
                ('Open', models.CharField(max_length=20, null=True, blank=True)),
                ('Close', models.CharField(max_length=20, null=True, blank=True)),
                ('High', models.CharField(max_length=20, null=True, blank=True)),
                ('Low', models.CharField(max_length=20, null=True, blank=True)),
                ('Adj_Close', models.CharField(max_length=20, null=True, blank=True)),
                ('Date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stocks_intraday',
            fields=[
                ('_id', models.AutoField(serialize=False, primary_key=True)),
                ('Ask', models.CharField(max_length=20, null=True, blank=True)),
                ('Symbol', models.CharField(max_length=20, blank=True)),
                ('AverageDailyVolume', models.CharField(max_length=20, null=True, blank=True)),
                ('Bid', models.CharField(max_length=20, null=True, blank=True)),
                ('AskRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('BidRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('Change', models.CharField(max_length=20, null=True)),
                ('Currency', models.CharField(max_length=20, null=True)),
                ('ChangeRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('AfterHoursChangeRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('DividendShare', models.CharField(max_length=20, null=True, blank=True)),
                ('LastTradeDate', models.CharField(max_length=20, null=True, blank=True)),
                ('TradeDate', models.CharField(max_length=20, null=True, blank=True)),
                ('EarningsShare', models.CharField(max_length=20, null=True, blank=True)),
                ('DaysLow', models.CharField(max_length=20, null=True, blank=True)),
                ('DaysHigh', models.CharField(max_length=20, null=True, blank=True)),
                ('YearLow', models.CharField(max_length=20, null=True, blank=True)),
                ('YearHigh', models.CharField(max_length=20, null=True, blank=True)),
                ('HoldingsGainRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('MoreInfo', models.CharField(max_length=20, null=True, blank=True)),
                ('OrderBookRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('MarketCapitalization', models.CharField(max_length=20, null=True, blank=True)),
                ('MarketCapRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('ChangeFromYearLow', models.CharField(max_length=20, null=True, blank=True)),
                ('PercentChangeFromYearLow', models.CharField(max_length=20, null=True, blank=True)),
                ('LastTradeRealtimeWithTime', models.CharField(max_length=20, null=True, blank=True)),
                ('ChangePercentRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('ChangeFromYearHigh', models.CharField(max_length=20, null=True, blank=True)),
                ('PercebtChangeFromYearHigh', models.CharField(max_length=20, null=True, blank=True)),
                ('LastTradeWithTime', models.CharField(max_length=20, null=True, blank=True)),
                ('LastTradePriceOnly', models.CharField(max_length=20, null=True, blank=True)),
                ('DaysRange', models.CharField(max_length=20, null=True, blank=True)),
                ('DaysRangeRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('FiftydayMovingAverage', models.CharField(max_length=20, null=True, blank=True)),
                ('ChangeFromFiftydayMovingAverage', models.CharField(max_length=20, null=True, blank=True)),
                ('PercentChangeFromFiftydayMovingAverage', models.CharField(max_length=20, null=True, blank=True)),
                ('Name', models.CharField(max_length=20, null=True, blank=True)),
                ('Open', models.CharField(max_length=20, null=True, blank=True)),
                ('PreviousClose', models.CharField(max_length=20, null=True, blank=True)),
                ('PricePaid', models.CharField(max_length=20, null=True, blank=True)),
                ('ChangeinPercent', models.CharField(max_length=20, null=True, blank=True)),
                ('PERatio', models.CharField(max_length=20, null=True, blank=True)),
                ('PERatioRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('LastTradeTime', models.CharField(max_length=20, null=True, blank=True)),
                ('Volume', models.CharField(max_length=20, null=True, blank=True)),
                ('YearRange', models.CharField(max_length=20, null=True, blank=True)),
                ('DaysValueChange', models.CharField(max_length=20, null=True, blank=True)),
                ('DaysValueChangeRealtime', models.CharField(max_length=20, null=True, blank=True)),
                ('StockExchange', models.CharField(max_length=20, null=True, blank=True)),
                ('PercentChange', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symbols',
            fields=[
                ('Symbol', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
    ]
