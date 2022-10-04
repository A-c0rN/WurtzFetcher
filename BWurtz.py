from requests import get
from bs4 import BeautifulSoup

url = "https://billwurtz.com/{}"


def getURLs(url):
    URLs = []
    data = None
    print("Fetching Wurtz Database", end="")
    with get(url) as r:
        print(".", end="")
        r.raise_for_status()
        print(".", end="")
        data = BeautifulSoup(r.text, "lxml")
    print(".", end="")
    if data:
        for link in data.find_all("a"):
            URLs.append(link.get("href"))
    print(" Done!")
    return URLs


def WurtzFetcher():
    boopy = []
    boof = getURLs(url=url.format("notebook.html"))
    for doot in boof:
        boopy.append(url.format(doot))
    return boopy


def billGetter(URLs):
    base = {}
    for url in URLs:
        name = url.split("/")[-1].split(".html")[0]
        data = ""
        print("Fetching Wurtz {}".format(name), end="")
        with get(url) as r:
            print(".", end="")
            r.raise_for_status()
            print(".", end="")
            data = r.text
            print(".", end="")
            base[name] = data
            print(" Done!")
    return base


def main():
    Wurtz = WurtzFetcher()
    heh = input(
        "There are {} Wurtzes. Depending on the count of Wurtz, this may take a hot sec. Get the Bills? [Y/n]:".format(
            str(len(Wurtz))
        )
    )
    if heh.lower() in ["y", "ye", "yes", "do", "do it", None, ""]:
        oof = billGetter(Wurtz)
        for key in oof.keys:
            print(key)


if __name__ == "__main__":
    main()
