import pytube
import os

print("Wolfy's YouTube Downloader")
print("version 0.4.0")

def mainMenu():
    print("===========================================================")
    print("Welcome to the main menu!")
    print("Please choose an option: ")
    print(" 1. Download first video from search")
    print(" 2. Download audio from title")
    print(" 3. Download video from URL")
    print(" 4. Download video playlist from URL")
    print(" 5. Download audio playlist from URL")
    print(" 6. Download Videos from URLS in videos.txt file")
    print(" 7. Download Audios from URLS in audios.txt file")

    usrChoice = input("Please make a choice: ")
    match usrChoice:
        case "1":
            print("===========================================================")
            searchDownload(input("Please enter your video title: "),"video")
            mainMenu()
        case "2":
            print("===========================================================")
            searchDownload(input("Please enter your audio title: "),"audio")
            mainMenu()
        case "3":
            print("===========================================================")
            downloadVideo(input("Please enter your video URL: "))
            mainMenu()
        case "4":
            print("===========================================================")
            downloadPlaylist(input("Please enter your playlist URL to download mp4: "),"video")
        case "5":
            print("===========================================================")
            downloadPlaylist((input("Please enter your playlist URL to download mp3: ")),"audio")
        case "6":
            print("===========================================================")
            print("Downloading videos from videos.txt")
            fileDownload("video")
            mainMenu()
        case "7":
            print("===========================================================")
            print("Downloading audios from audios.txt")
            fileDownload("audio")
            mainMenu()
        case _:
            print ("unknown command!")
            mainMenu()
        
        
def searchDownload(searchQuery, downloadformat):
    try:
        searchVideo = pytube.Search(searchQuery)
        if downloadformat == "video":
            downloadVideo(searchVideo.results[0].watch_url,"video")
        elif downloadformat == "audio":
            downloadVideo(searchVideo.results[0].watch_url, "audio")
    except:
        print("An error occured searching for the video!")

def downloadVideo(vidURL, format):
    try:
        yt = pytube.YouTube(vidURL)
        if format == "video":
            print("Downloading", yt.title)
            yt.streams.get_highest_resolution().download()
            print("Downloaded video!")
        elif format == "audio":
            print("Downloading", yt.title)
            yt.streams.filter(only_audio=True).first().download(filename=yt.title+".mp3")
            print("Downloaded audio!")
    except:
        print("error downloading")

def downloadPlaylist(playlistURL, fileFormat):
    try:
        vidPlaylist = pytube.Playlist(playlistURL)

        if fileFormat == "video":
            for ytVideo in vidPlaylist.videos:
                downloadVideo(ytVideo.watch_url,"video")
        elif fileFormat == "audio":
            for ytMusic in vidPlaylist.videos:
                downloadVideo(ytMusic.watch_url,"audio")
        
        print("Download process completed!")
        mainMenu()
    except:
        print("An error occured whilst downloading your playlist!")
        mainMenu()

def fileDownload(fileFormat):
    try:
        if fileFormat == "video":
            videoList = open("videos.txt","r")
            videoURLS = str(videoList.read()).splitlines()
            for f in videoURLS:
                if f != "":
                    downloadVideo(f, "video")
        if fileFormat == "audio":
            AudioList = open("audios.txt","r")
            AudioURLS = str(videoList.read()).splitlines()
            for f in videoURLS:
                if f != "":
                    downloadVideo(f, "audio")
    except:
        print("An error occured!")
        print("Please ensure URLs are correct & the files exists!")


# main code
if __name__ == '__main__':
    mainMenu()