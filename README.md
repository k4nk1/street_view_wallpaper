# Street View Wallpaper
## Description
An app to set random Google Street View in the world as a wallpaper.
## How to use
1. Clone this repository.
```
> git clone https://github.com/k4nk1/street-view-wallpaper.git
```

2. Install dependencies.
```
> cd street-view-wallpaper
> uv sync
```

3. Fix an issue in street_view_randomizer according to https://github.com/diegopaiva1/street-view-randomizer/issues/1.

4. Run update.py to change the wallpaper.
```
> uv run update.py
```

5. Run open.py to visit the place of the wallpaper in Google Maps.
```
> uv run open.py
```

## Notes
- Use task scheduler to run update.py on a regular basis.
- This app only works on Windows currently.
- You can specify the image to visit.
```
> uv run open.py ./images/ind/23.90173713532966,93.21111447554931.jpg
```
- This app needs Google Maps API key, so get your key in https://developers.google.com/maps/documentation/streetview/overview and set the key as environment variable 'GOOGLE_MAPS_API_KEY'
- Unfortunately, the API only allows you to get images up to 640px in size, so the images will be pixelated.
