from hulu_api import get_shows, get_videos_for_show, check_login_token, get_search_results
from XML_Utils import get_xml_node
from hulu_objects import Item_List, Video
try:
    import L, XML, Callback, Data, Redirect, Datetime, WebVideoURL, PopupDirectoryObject, CACHE_1HOUR, InputDirectoryItem, InputDirectoryObject, PrefsItem, Dict, MessageContainer, Function, DirectoryObject, MediaContainer, VideoItem, DirectoryItem, EpisodeObject, Ex, Hash, HTML, HTTP, handler, JSON, Log, MovieObject, NextPageObject, ObjectContainer, parallelize, Plugin, Prefs, PrefsObject, Regex, Resource, route, SeasonObject, SearchDirectoryObject, String, task, TVShowObject, VideoClipObject  # @UnresolvedImport # pylint: disable=F0401
except ImportError:
    # Skip dummy import
    pass
VALID_PER_PAGE_PREFS = ["10", "25", "50"]
VIDEO_PREFIX = "/video/hulu"
NAME = L('Title')
NAME = "Hulu"

ART = 'art-default.jpg'
ICON = 'icon-default.png'

####################################################################################################

def Start():

    # # make this plugin show up in the 'Video' section
    # # in Plex. The L() function pulls the string out of the strings
    # # file in the Contents/Strings/ folder in the bundle
    # # see also:
    # #  http://dev.plexapp.com/docs/mod_Plugin.html
    # #  http://dev.plexapp.com/docs/Bundle.html#the-strings-directory
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    # # set some defaults so that you don't have to
    # # pass these parameters to these object types
    # # every single time
    # # see also:
    # #  http://dev.plexapp.com/docs/Objects.html
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = Resource.Load(ART)
    DirectoryItem.thumb = Resource.Load(ICON)
    VideoItem.thumb = Resource.Load(ICON)

    HTTP.CacheTime = CACHE_1HOUR
    check_login_token()




# see:
#  http://dev.plexapp.com/docs/Functions.html#ValidatePrefs
def ValidatePrefs():
    error_message = None
    u = Prefs['username']
    p = Prefs['password']
    items_per_page = Prefs['items_per_page']
    if items_per_page in VALID_PER_PAGE_PREFS:
        error_message = "Invalid setting for number of items per page."
    # # do some checks and return a
    # # message container
    if (u and p):
        return MessageContainer("Success", "User and password OK.")
    if error_message:
        error_message = "You need to provide both a username and password."





#### the rest of these are user created functions and
#### are not reserved by the plugin framework.
#### see: http://dev.plexapp.com/docs/Functions.html for
#### a list of reserved functions above



#
# Example main menu referenced in the Start() method
# for the 'Video' prefix handler
#
# 
# def VideoMainMenu():
# 
#     # Container acting sort of like a folder on
#     # a file system containing other things like
#     # "sub-folders", videos, music, etc
#     # see:
#     #  http://dev.plexapp.com/docs/Objects.html#MediaContainer
#     dir = MediaContainer(viewGroup="InfoList")
# 
# 
#     # see:
#     #  http://dev.plexapp.com/docs/Objects.html#DirectoryItem
#     #  http://dev.plexapp.com/docs/Objects.html#function-objects
#     dir.Append(
#         Function(
#             DirectoryItem(
#                 CallbackExample,
#                 "directory item title",
#                 subtitle="subtitle",
#                 summary="clicking on me will call CallbackExample",
#                 thumb=Resource(ICON),
#                 art=Resource(ART)
#             )
#         )
#     )
# 
#     # Part of the "search" example
#     # see also:
#     #   http://dev.plexapp.com/docs/Objects.html#InputDirectoryItem
#     dir.Append(
#         Function(
#             InputDirectoryItem(
#                 SearchResults,
#                 "Search title",
#                 "Search subtitle",
#                 summary="This lets you search stuff",
#                 thumb=Resource(ICON),
#                 art=Resource(ART)
#             )
#         )
#     )
# 
# 
#     # Part of the "preferences" example
#     # see also:
#     #  http://dev.plexapp.com/docs/Objects.html#PrefsItem
#     #  http://dev.plexapp.com/docs/Functions.html#CreatePrefs
#     #  http://dev.plexapp.com/docs/Functions.html#ValidatePrefs
#     dir.Append(
#         PrefsItem(
#             title="Your preferences",
#             subtile="So you can set preferences",
#             summary="lets you set preferences",
#             thumb=Resource(ICON)
#         )
#     )
# 
#     # ... and then return the container
#     return dir
# 
# def CallbackExample(sender):
# 
#     # # you might want to try making me return a MediaContainer
#     # # containing a list of DirectoryItems to see what happens =)
# 
#     return MessageContainer(
#         "Not implemented",
#         "In real life, you'll make more than one callback,\nand you'll do something useful.\nsender.itemTitle=%s" % sender.itemTitle
#     )

# Part of the "search" example
# query will contain the string that the user entered
# see also:
#   http://dev.plexapp.com/docs/Objects.html#InputDirectoryItem
def SearchResultsMenu(query, page_number=1):
    # http://m.hulu.com/search?dp_identifier=hulu&query=doctor&items_per_page=10&page=1&format=xml
    oc = ObjectContainer(no_cache=True)
    for video in get_search_results(query, page_number):
        oc.add(video)

    if len(oc) < 1:
        return ObjectContainer(header="Not found", message="Could not find any results for the search string '{}'.".format(query))

    return oc


def ShowVideos(show_id):
    oc = ObjectContainer()
    show_videos = get_videos_for_show(show_id)
    for video in show_videos:
        Log.Debug("Adding video %s", video.title)
        oc.add(EpisodeObject(
                rating_key=video.get_thumbnail_url(),
                key=WebVideoURL(video.get_embed_url()),
                title=video.title,
                summary=video.description,
                thumb=Resource.ContentsOfURLWithFallback(video.get_thumbnail_url()))
            )
        Log.Debug("Done adding video %s", video.title)
    return oc

@handler(VIDEO_PREFIX, NAME)
def MainMenu():

        oc = ObjectContainer()
        oc.add(InputDirectoryObject(key=Callback(SearchResultsMenu), title="Search", prompt="Search for a Stream", summary="Search for a Stream"))
        oc.add(DirectoryObject(key=Callback(TV_Shows), title="TV Shows"))
        oc.add(PrefsObject(title="Preferences"))

        return oc



####################################################################################################
@route(VIDEO_PREFIX + '/tv_shows')
def TV_Shows():

    oc = ObjectContainer(title2="TV Shows", no_cache=True)
    shows = get_shows()
    Log.Debug("Got %s shows", len(shows))
    for show in shows:
        Log.Debug("Adding show '%s', ID '%s'.", show.name, show.id)
        rating_key = show.company_id   + "_" + show.id
        show_item = TVShowObject(thumb=show.get_thumbnail_url(),title=show.name, summary=show.description, rating_key=rating_key, key=Callback(ShowVideos, show_id=show.id))
        oc.add(show_item)
        Log.Debug("Added show '%s', ID '%s'.", show.name, show.id)
    return oc



