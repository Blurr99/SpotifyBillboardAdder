# SpotifyBillboardAdder

What this project does is that, first it asks for spotify authentication from the currently logged in spotify account. 

After authenticating spotify access, it asks for a date in a YYYY-MM-DD format as follows:

![image](https://github.com/Blurr99/SpotifyBillboardAdder/assets/116642733/eb504a06-583d-4d73-815b-0db5cc7e0f9d)


Afterwards it goes to the official <a href="https://www.billboard.com/charts/hot-100/2023-07-01/">Spotify Billboard</a> listing for the period of that date:

![image](https://github.com/Blurr99/SpotifyBillboardAdder/assets/116642733/a64372a7-9f28-451e-8de3-df4c176b63b3)


It then scrapes the names of the songs along with their artists in a Python list and then uses the <a href="https://pypi.org/project/spotify/">Spotipy library</a> to sook up the URIs(used by spotify to uniquely identify each song) for all of the songs:

![image](https://github.com/Blurr99/SpotifyBillboardAdder/assets/116642733/dafe2b85-a0f6-4979-95f4-2f9ee4f33369)


and if the URI for that songs are depricated, it says that song wasnt found on spotify:

![image](https://github.com/Blurr99/SpotifyBillboardAdder/assets/116642733/c8dbfc7f-d73c-4efe-8ba3-463575767f27)


It then creates a playlist from the currently logged in spotify account and adds all the songs from the billboard list:

![image](https://github.com/Blurr99/SpotifyBillboardAdder/assets/116642733/2a78b679-f6ea-4094-9c77-ea827453f866)


![image](https://github.com/Blurr99/SpotifyBillboardAdder/assets/116642733/7bf90fb9-29ce-4776-a180-6e7b937423dd)


Steps to to run this program on a different code:
<ol>
  <li> Download the main.py file and the token.txt file into a single folder </li>
  <li> Go to <a href="https://developer.spotify.com">Spotify for developers site</a> and get the required keys such as access token, clientID, client secret key etc. and use them in the main and token files</li>
  <li> Run your code</li>
</ol>









