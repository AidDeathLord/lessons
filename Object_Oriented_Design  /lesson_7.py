from datetime import date, timedelta


class Booking():
    register = []

    def book(self, first_date, second_date):
        f_date = date.fromisoformat(first_date)
        s_date = date.fromisoformat(second_date)
        if f_date > s_date:
            return False
        if f_date == s_date:
            return False
        if f_date in Booking.register:
            a = f_date + timedelta(days=1)
            if a in Booking.register:
                return False
        Booking.register.append(f_date)
        while f_date < s_date:
            f_date += timedelta(days=1)
            if f_date in Booking.register:
                continue
            Booking.register.append(f_date)
        return True


booking = Booking()
assert not booking.book('2008-11-10', '2008-11-05')
assert booking.book('2008-11-11', '2008-11-13')
assert not booking.book('2008-11-12', '2008-11-12')
assert not booking.book('2008-11-12', '2008-11-14')
print(booking.register)
assert booking.book('2008-11-10', '2008-11-11')
assert not booking.book('2008-11-12', '2008-11-13')
assert not booking.book('2008-11-13', '2008-11-13')
print(booking.register)
assert booking.book('2008-11-13', '2008-11-14')
assert booking.book('2008-05-08', '2008-05-18')
assert not booking.book('2008-05-09', '2008-05-10')

# assert not booking.book('2008-11-10', '2008-11-05')
# assert booking.book('2008-11-11', '2008-11-13')
