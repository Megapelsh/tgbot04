import webbrowser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbconn import engine, Base, Vehicle, User

session = sessionmaker(bind=engine)
s = session()

user_one = User(phone='+380974041610')
s.add(user_one)
s.commit()

user_one = User(phone='+380955811474', password='123456')
s.add(user_one)
s.commit()

s.add_all([Vehicle(brand='Skoda', model='Octavia', fuel='бензин/газ', engine='1.6', year='2007', vin='777777777777', user_id='1', token='f789'),
           Vehicle(brand='Volvo', model='XC90', fuel='бензин', engine='3.5', year='2017', vin='888888888888', user_id='2')
           ])
s.commit()


print(s.query(User).first().phone)

for phone, id in s.query(User.phone, User.id).order_by(User.id).limit(2):
    print(row.Users.id, ' ', row.Users.phone)

print('\n\n\n')

print([(row.Users.id, row.Users.phone) for row in s.query(User, Vehicle).join(Vehicle).all()])

