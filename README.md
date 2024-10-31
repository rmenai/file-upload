<!-- ABOUT THE PROJECT -->

## About The Project

So I was looking for a great server with an API for storing my files. I tried multiple ones but they all have the same
problem: They are not fast enough. That's why I decide to make my own, a simple and very fast one.

### Built With

* [Python](https://www.python.org)
* [FastAPI](https://fastapi.tiangolo.com/)

<!-- GETTING STARTED -->

## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rmenai007/file-upload.git
   ```
2. Install the python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Now install [python-dotenv](https://pypi.org/project/python-dotenv/)
   ```sh
   pip install python-dotenv
   ```
4. Create a file called .env then enter your API key
   ```JS
   API_KEY = 'ENTER YOUR API'
   ```

<!-- USAGE EXAMPLES -->

## Usage

This is an example in Python:
```python
class FileUpload:
    def __init__(self, api_key: str):
        self.url = "https://file-upload.rmenai007.repl.co"  # Host your server then change the url here
        self.key = api_key

        self.files = {}

    def upload(self, file_path: str, folder: str = "") -> Union[int, str]:
        """Uploads a file to the server"""

        params = {"key": self.key, "folder": folder}
        files = {"file": open(file_path, "rb")}
        r = requests.post(f"{self.url}/api/v1/upload", params=params, files=files)

        if r.ok:
            value = r.json()
            self.files[value["id"]] = value["url"]

            return value["id"]

        raise HTTPError(r.json()["detail"])

    def view(self, file_id: str) -> str:
        """Gets the file url from id"""

        return self.files[file_id]

    def delete(self, file_id: str) -> int:
        """Deletes the file from the server"""

        params = {"key": self.key, "id": file_id}
        r = requests.delete(f"{self.url}/api/v1/delete", params=params)

        return r.status_code
```

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge

[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge

[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members

[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge

[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge

[issues-url]: https://github.com/othneildrew/Best-README-Template/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/othneildrew
