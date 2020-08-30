# REST API for Movie Booking

This is an API service for Movie Theatre Ticket Booking

## Install

    pip install -r requirements.txt

## Run the app

    python manage.py runserver

## Run the tests

    ./run-tests.sh

# Solution Approach

-   An endpoint to book a ticket using a user’s name, phone number, and timings. [Solution](#1)
-   An endpoint to update a ticket timing. [Solution](#2)
-   An endpoint to view all the tickets for a particular time. [Solution](#3)
-   An endpoint to delete a particular ticket. [Solution](#4)
-   An endpoint to view the user’s details based on the ticket id. [Solution](#5)
-   Mark a ticket as expired if there is a diff of 8 hours between the ticket timing and current time. [Solution](#6)
-   Delete all the tickets which are expired automatically.
-   Write the tests for all the endpoints. [Solution](#7)

# REST API

## Get list of Customers

### Request <a name = "1"></a>

`GET /api/customers/`

### Example

    curl --location --request GET 'http://127.0.0.1:8000/api/customers/'

#### Response

    [
        {
            "id": "b22e55e0-e4ed-4265-b702-47c1622e439c",
            "username": "Dheeraj",
            "phone": "+919711835404"
        },
        {
            "id": "18434971-80dd-4c66-abb4-e7d9617da19f",
            "username": "Uma",
            "phone": "+919968251251"
        },
        {
            "id": "c61660a7-10c6-4a4a-aaa8-6aef9e5d818c",
            "username": "Bhawna",
            "phone": "+918447761028"
        }
    ]

## Get details of customer using Ticket Id

### Request

`GET /api/customers/<ticketid>`

### Example

    curl --location --request GET 'http://127.0.0.1:8000/api/customers/fc0223d3-eaa6-4fa8-81a1-b7ff8283298e'

#### Response

    [
        {
            "id": "b22e55e0-e4ed-4265-b702-47c1622e439c",
            "username": "Dheeraj",
            "phone": "+919711835404"
        }
    ]

## Get TicketId for the using Show timings

### Request

`GET /api/ticket?time=<%H:%M:%S %Y-%m-%d>`

### Example

    curl --location --request GET 'http://127.0.0.1:8000/api/ticket?time=14:54:55%202020-08-31'

#### Response

    [
        {
            "TicketId": "fc0223d3-eaa6-4fa8-81a1-b7ff8283298e",
            "ShowId": "e095afdd-0e7a-4eef-bcdb-4f613bd3224b",
            "CustomerId": "b22e55e0-e4ed-4265-b702-47c1622e439c"
        }
    ]

## Book a ticket

### Request

`POST /api/ticket/`

### Payload

    {
        phone,
        username (optional, only required if the user is not registered),
        starttime,
        moviename
    }

### Example

    curl --location --request POST 'http://127.0.0.1:8000/api/ticket/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "phone": "+919711835404",
        "username": "Dheeraj",
        "moviename": "Om Shanti Om",
        "starttime" : "14:54:55 2020-08-31"
    }'

#### Response

    {
        "TicketId": "34f58ebd-b512-4981-8604-94556b5b9324"
    }

## Delete Ticket using Tid

### Request

`DELETE /api/ticket/<ticketid>/`

### Example

    curl --location --request DELETE 'http://127.0.0.1:8000/api/ticket/34f58ebd-b512-4981-8604-94556b5b9324'

#### Response

    {
        "Message": "Deleted Ticket with Tid: 34f58ebd-b512-4981-8604-94556b5b9324"
    }

## Update Show timings for a given Ticket

### Request

`PUT /api/ticket/<ticketid>/`

### Payload

    {
        "time" (format : %H:%M:%S %Y-%m-%d)
    }

### Example

    curl --location --request PUT 'http://127.0.0.1:8000/api/ticket/fc0223d3-eaa6-4fa8-81a1-b7ff8283298e' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "time" : "14:54:55 2020-08-29"
    }'

#### Response

    {
        "Message"   :   "Updated timing for this ticket to 14:54:55 2020-08-29"
    }

## View shows

### Request

`GET /api/shows/`

#### Query Params

    {
        all : true/false  (required),
        time : (format : %H:%M:%S %Y-%m-%d)
    }

### Example

    curl --location --request GET 'http://127.0.0.1:8000/api/shows/?all=true' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "time" : "14:54:55 2020-08-29"
    }'

### Response

    [
        {
            "showid": "720dc4f5-1df2-4686-8f31-702aca10e9f9",
            "MovieName": "Om Shanti Om",
            "Screen": "2",
            "Duration": "180",
            "StartTime": "2020-08-30T16:13:36Z",
            "count": 20,
            "IsExpired": false
        }
    ]

## Mark tickets as expired

### Request

`PUT /api/expired/`

### Example

    curl --location --request PUT 'http://127.0.0.1:8000/api/expired/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "time" : "14:54:55 2020-08-29"
    }'

### Response

    (Active tickets)
    [
        {
            "showid": "720dc4f5-1df2-4686-8f31-702aca10e9f9",
            "MovieName": "Om Shanti Om",
            "Screen": "2",
            "Duration": "180",
            "StartTime": "2020-08-30T16:13:36Z",
            "count": 20,
            "IsExpired": false
        }
    ]

## Delete expired tickets

### Request

`DELETE /api/expired/`

### Example

    curl --location --request DELETE 'http://127.0.0.1:8000/api/expired/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "time" : "14:54:55 2020-08-29"
    }'

### Response

    (All Tickets)
    [
    {
        "showid": "720dc4f5-1df2-4686-8f31-702aca10e9f9",
        "MovieName": "Om Shanti Om",
        "Screen": "2",
        "Duration": "180",
        "StartTime": "2020-08-30T16:13:36Z",
        "count": 20,
        "IsExpired": false
    }
    ]
