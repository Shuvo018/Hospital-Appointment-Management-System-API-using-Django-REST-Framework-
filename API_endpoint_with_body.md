##  Register

http://127.0.0.1:8000/accounts/register/

```bash
{
    "username": "shuvo",
    "email": "shuvodevnath0188@gmail.com",
    "first_name": "doctor",
    "last_name": "abc",
    "role": "DOCTOR",
    "password": "apple1234",
    "phone_number": "1234536"
}
```

## login

http://127.0.0.1:8000/accounts/login/


```bash
{
    "email": "shuvodevnath0188@gmail.com",
    "password": "banana1234"
}
```

## logout

http://127.0.0.1:8000/accounts/logout/

```bash
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4NDU2NTM2OCwiaWF0IjoxNzg0NDc4OTY4LCJqdGkiOiIxNmFmMzhjOTRiMTQ0MmUyYjQyMDRmYTZhNDI3MmU0OCIsInVzZXJfaWQiOiI2In0.3ugYuA-5wCSv8MIH8mJGRt0xNf9bKCaOjUVhcUSq71U"
}
```


## Forgot password

http://127.0.0.1:8000/accounts/forgot-password/

```bash
{
    "email": "shuvodevnath0188@gmail.com"
}
```

## Reset password

http://127.0.0.1:8000/accounts/reset-password/

```bash
{
    "uid": "OQ&",
    "token": "dbzk32-69307abfeee40e4879f808263cb90b45",
    "password": "banana1234"
}
```


## create doctor

http://127.0.0.1:8000/doctors/create/

```bash
{
    "user": 7,
    "name": "John Doe",
    "department": "Cardiology",
    "specialization": "Heart Specialist",
    "visiting_fee": 800
}
```

## doctors list

http://127.0.0.1:8000/doctors/

## get doctor

http://127.0.0.1:8000/doctors/1/

## update doctor

http://127.0.0.1:8000/doctors/1/

```bash
{
    "id": 1,
    "name": "doctor nil",
    "department": "depart abcd",
    "specialization": "something Specialization",
    "visiting_fee": "1000.00",
    "email": "doctor01@gmail.com",
    "phone_number": "0188850775"
}
```

## patch doctor

http://127.0.0.1:8000/doctors/1/

```bash
{
    "department": "depart abcd"
}
```

## add appointment

http://127.0.0.1:8000/appointments/

```bash
{
    "patient": 2,
    "doctor": 3,
    "appointment_date": "2026-07-18",
    "appointment_time": "18:45:48",
    "status": "PENDING"
}
```

## appointment list

http://127.0.0.1:8000/appointments/

## update appointment

http://127.0.0.1:8000/appointments/1/

```bash
{
    "patient": 2,
    "doctor": 1,
    "appointment_date": "2026-07-22",
    "appointment_time": "18:45:48",
    "status": "PENDING"
}
```