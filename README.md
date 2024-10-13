# lab2_req

This Flask web application is designed to collect user data through a simple form, validate the inputs, and display a personalized confirmation message. It includes both backend logic and front-end design elements, ensuring a smooth user experience.

The application starts with the main `app.py` file, which sets up two routes: the home page (`/`) where users can fill out a form, and the submission route (`/submit`), which processes the form data and displays a thank-you page with the submitted name and email. The form is built using HTML in the `home.html` template and styled with an external CSS file. On submission, the data is passed to the server using the POST method, and the result is rendered dynamically on a new page using the `result.html` template, where Flask's Jinja2 templating engine inserts the user’s name and email.

The front-end of the application is styled using an external CSS file (`style.css`), which makes the form responsive and visually appealing. The form fields and submit button are styled to ensure usability across devices, with additional focus states for improved interaction. The CSS also includes media queries to ensure that the layout adapts well to different screen sizes.

Overall, this app demonstrates a combination of Flask for backend logic, Jinja2 for dynamic content rendering, and modern HTML and CSS for creating a responsive and user-friendly interface.
