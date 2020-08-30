-   ## Add Shows

    ### Request

    `POST /api/addshows/`
    <img src="img/AddShows.jpg" style=""/>

-   ## Get list of Customers

    ### Request

    `GET /api/customers/`
    <img src="img/GetAllCustomers.jpg" style=""/>

-   ## Get details of customer using Ticket Id <a name = "5"></a>

    ### Request

    `GET /api/customers/<ticketid>`
    <img src="img/GetCustomerbyId.jpg" style=""/>

-   ## Get TicketId for the using Show timings

    ### Request

    `GET /api/ticket?time=<%H:%M:%S %Y-%m-%d>`
    <img src="img/GetTicketbyTime.jpg" style=""/>

-   ## Book a ticket <a name = "1"></a>

    ### Request

    `POST /api/ticket/`

      <img src="img/BookTicket.jpg" style=""/>

-   ## Delete Ticket using Tid <a name = "4"></a>

    ### Request

    `DELETE /api/ticket/<ticketid>/`
    <img src="img/DeleteTicketbyTid.jpg" style=""/>

-   ## Update Show timings for a given Ticket <a name = "2"></a>

    ### Request

    `PUT /api/ticket/<ticketid>/`
    <img src="img/UpdateTicketTime.jpg" style=""/>

-   ## View shows (All/Particular TIme) <a name = "3"></a>

    ### Request

    `GET /api/shows/`

    All Shows

    <img src="img/ShowAllShows.jpg" style=""/>

    Shows by time

    <img src="img/ShowShowsbyTimings.jpg" style=""/>
