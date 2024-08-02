## Flask Application Design

### HTML Files

- **index.html**: The main HTML file that serves as the user interface. It contains the form for entering event details and the button to create the events.
- **sidebar.html**: A separate HTML file that includes the configuration options for the application (e.g., selecting the calendar, mapping sheet columns to event fields). This can be loaded as a modal or a persistent sidebar.

### Routes

- **route_create_events**: This route handles the POST request from the form submission. It extracts event details from the request, creates Google Calendar events, and returns a response.
- **route_update_config**: This route handles POST requests from the configuration sidebar. It updates the application's configuration based on the user's inputs and returns a response.
- **route_get_config**: This route handles GET requests for the current configuration. It returns a JSON response containing the configuration values.