import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ISBNLookupView(APIView):
    def get(self, request, isbn):
        try:
            # Main book data
            book_url = f"https://openlibrary.org/isbn/{isbn}.json"
            book_response = requests.get(book_url)
            if book_response.status_code != 200:
                return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

            book_data = book_response.json()

            # Get author names
            author_names = []
            for author in book_data.get("authors", []):
                author_key = author.get("key")
                if author_key:
                    author_res = requests.get(f"https://openlibrary.org{author_key}.json")
                    if author_res.status_code == 200:
                        author_names.append(author_res.json().get("name", "Unknown"))

            return Response({
                "title": book_data.get("title"),
                "authors": author_names,
                "publisher": book_data.get("publishers", [None])[0],
                "publish_date": book_data.get("publish_date"),
            })

        except Exception as e:
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)