# from datetime import datetime
# def show(year,date,month):
#     pass
# def main():
#     current_date = datetime.now()
#     birthdate = datetime(year, month, day)
#
#     from datetime import datetime
#
#     def calculate_age(birthdate):
#         today = datetime.now()
#         age = today.year - birthdate.year - (
#                     today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day))
#         return age
#
#     # Example usage
#     birthdate = datetime(1990, 5, 15)
#
#     age = calculate_age(birthdate)
#     print(f"The person is {age} years old.")

# from datetime import datetime
# from dateutil import relativedelta
#
#
# def show(year,month,day):                               #2000   10   11
#     dob = day + "/" + month + "/" + year                #2000/10/11
#     curr = "18/1/2024"
#
#     dob = datetime.strptime(dob,"%d/%m/%Y")
#     curr = datetime.strptime(curr,"%d/%m/%Y")
#
#     diff = relativedelta.relativedelta(curr,dob)
#
#     print("year = ",diff.years)
#     print("month ",diff.months)
#     print("days ",diff.days)
#
#
# def main():
#     year = input("Enter year ")
#     month = input("Enter month ")
#     day = input("Enter day ")
#     show(year,month,day)
#
# main()





