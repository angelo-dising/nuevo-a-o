from datetime import timedelta, datetime
import time

print()
print('* NEW YEAR COUNTDOWN *')
print('  (Exit with CTRL + C)')
print()

try:
    while True:
        date_now  = datetime.today()
        date_now_timestamp = int(date_now.timestamp())
        new_year_date = datetime(year=date_now.year + 1, month=1, day=1, hour=0, minute=0, second=0)
        new_year_timestamp = int(new_year_date.timestamp())
        remaining_time_seconds = new_year_timestamp - date_now_timestamp

        remaining_time = timedelta(seconds=remaining_time_seconds)
        remaining_days = remaining_time.days
        remaining_seconds = remaining_time.seconds

        remaining_minutes, remaining_seconds = divmod(remaining_seconds, 60)
        remaining_hours, remaining_minutes = divmod(remaining_minutes, 60)

        if remaining_days:
            if remaining_days > 1:
                remaining_days = '{} days'.format(remaining_days)
            else:
                remaining_days = '{} day'.format(remaining_days)
        else:
            remaining_days = ''


        if remaining_hours:
            if remaining_hours > 1:
                remaining_hours = ', {} hours'.format(remaining_hours)
            else:
                remaining_hours = ', {} hour'.format(remaining_hours)
        else:
            remaining_hours = ''


        if remaining_minutes:
            if remaining_minutes > 1:
                remaining_minutes = ', {} minutes'.format(remaining_minutes)
            else:
                remaining_minutes = ', {} minute'.format(remaining_minutes)
        else:
            remaining_minutes = ''


        if remaining_seconds:
            if remaining_seconds > 1:
                remaining_seconds = ', {} seconds'.format(remaining_seconds)
            else:
                remaining_seconds = ', {} second'.format(remaining_seconds)
        else:
            remaining_seconds = ''

        # print('Time remaining: {}{}{}{}'.format(remaining_days,
        #                                         remaining_hours,
        #                                         remaining_minutes,
        #                                         remaining_seconds))

        spaces = '                                    '

        print('\rTime remaining: {}{}{}{}{}'.format(remaining_days,
                                                remaining_hours,
                                                remaining_minutes,
                                                remaining_seconds,
                                                spaces), end='')                                        

        time.sleep(1)

except KeyboardInterrupt:
    exit()