import datetime
import calendar

def translator(day_name):
    match day_name:
        case 'Monday':
            return 'Poniedzialek'
        case 'Tuesday':
            return 'Wtorek'
        case 'Wednesday':
            return "Środa"
        case 'Thursday':
            return 'Czwartek'
        case 'Friday':
            return 'Piątek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'

date_of_birth = input("Podaj date urodzin typu 1-1-2000: ")

day, month, year = date_of_birth.split("-") # (1, 1, 2000)

date_of_birth = datetime.datetime(int(year), int(month), int(day))

day_name = calendar.day_name[date_of_birth.weekday()]
print(translator(day_name))