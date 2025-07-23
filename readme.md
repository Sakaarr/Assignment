✅ Project Overview: ISBN Book Search App
The ISBN Book Search App is a full-stack web application that allows users to search for books using ISBN numbers and retrieve key details such as:

📖 Title

✍️ Author(s)

🏢 Publisher

📅 Publish date

The app fetches real-time book data using the Open Library API, providing a clean and intuitive interface for users to explore bibliographic info with a single input.

🧱 Tech Stack
Layer	        Technology
Frontend	 React (Create React App)
Backend	     Django + Django REST Framework
API	         OpenLibrary API
HTTP	     Axios (frontend) + Requests (backend)

🧪 How it Works
User enters a valid ISBN-10 or ISBN-13 number in the frontend UI.

The React app sends a request to the Django API backend.

The backend uses the ISBN to call the Open Library API, fetches the book data, and resolves author names.

Formatted data is returned to the frontend and displayed to the user.

🌍 Deployment
Component	Platform	URL
Frontend	Vercel	    https://assignment-theta-ten.vercel.app/
Backend	PythonAnywhere	https://sakar.pythonanywhere.com/api/books/lookup/{isbn}

✅ Both the frontend and backend are publicly accessible and connected properly.

📖 API Transparency
Uses Open Library’s ISBN endpoint

Resolves author names via separate author key lookup

No authentication or paid services used — entirely public and open-source

📘 Use Case
Ideal for:

Book lookup tools

Library catalog apps

Education, reading list generators, etc.