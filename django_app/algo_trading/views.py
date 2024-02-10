from django.shortcuts import render, redirect
from .forms import CSVImportForm
from .models import HistoricalData, HistoricalDataNSE
import csv
from django.contrib.auth.decorators import login_required
from .stratergies import Stratergy
import yfinance as yf
from datetime import datetime
from .data_scraper import NSE


@login_required
def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                HistoricalData.objects.create(
                    date=row['date'],
                    open=row['open'],
                    high=row['high'],
                    low=row['low'],
                    close=row['close'],
                )

            return render(request, 'success.html', {'context': 'success'})
    else:
        form = CSVImportForm()

    return render(request, 'import.html', {'form': form})


@login_required
def success_page(request):
    return render(request, 'success.html', {'context': 'success'})


def prediction_model(request):
    historical_data = HistoricalData.objects.all()
    data_1 = {}

    date_array = []
    open_array = []
    high_array = []
    low_array = []
    close_array = []
    for elem in historical_data:
        date_array.append(elem.date)
        open_array.append(elem.open)
        high_array.append(elem.high)
        low_array.append(elem.low)
        close_array.append(elem.close)

    data_1 = {
        'date': date_array,
        'open': open_array,
        'high': high_array,
        'low': low_array,
        'close': close_array,
    }
    context = []
    context = Stratergy(historical_data=data_1).stratergy_1()
    return render(request, 'output.html', {'context': context})


def get_nse_historical_data(request):
    HistoricalDataNSE.objects.all().delete()
    current_date = datetime.today().strftime('%Y-%m-%d')
    ticker = ['RELIANCE.NS', 'SBIN.NS', 'AXISBANK.NS', 'TATAPOWER.NS', 'TCS.NS', 'INFY.NS', 'WIPRO.NS', 'LUPIN.NS', 'BPCL.NS']
    data = []
    # tz = pytz.timezone("Asia/Kolkata")
    try:
        data = yf.download(ticker, '2010-01-01', current_date)
        data.reset_index(inplace=True)
        for item in ticker:
            for index, row in data.iterrows():
                HistoricalDataNSE.objects.create(
                    ticker=item,
                    date=row['Date'],
                    open=row[('Open', item)],
                    high=row[('High', item)],
                    low=row[('Low', item)],
                    close=row[('Close', item)],
                    adj_close=row[('Adj Close', item)],
                    volume=row[('Volume', item)]
                )
        return render(request, 'success.html', {'context': 'success'})
    except Exception as e:
        return render(request, 'success.html', {'context': e})


def live_data():
    try:
        nse = NSE()
        nse.live_data()
    except Exception as e:
        print(e)
        pass
