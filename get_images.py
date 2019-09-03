from google_images_download import google_images_download

def main():
    SEARCH_ELEM = ["Famous abstract art", "mountains"]
    client = google_images_download.googleimagesdownload()

    for elem in SEARCH_ELEM:
        
        arguments = {
            "keywords": elem, 
            "limit": 100, 
            "print_urls": True, 
            "output_directory": "images",
            "image_directory": elem
        }        
        paths = client.download(arguments)
        print(paths)

if __name__ == '__main__':
    main()
