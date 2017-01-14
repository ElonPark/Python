# import report
#
# description  = report.get_description()
# print("Today's weather:", description)
# import report as wr
# description  = wr.get_description()
# print("Today's weather:", description)
# from report import get_description as do_it
# description  = do_it()
# print("Today's weather:", description)
from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
