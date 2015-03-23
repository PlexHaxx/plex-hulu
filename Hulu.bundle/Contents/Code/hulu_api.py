import operator
import time
import re
import urllib
from XML_Utils import get_xml_node
from hulu_objects import Item_List, Show, Video
BASE_URL = "http://m.hulu.com/"
LOGIN_QUEUE_TOKEN_NAME = "login_queue_token"
HULU_SEARCH_URL = BASE_URL + "search?dp_identifier=hulu&query=%s&items_per_page=%s&page=%s&format=xml"

try:
    import XML, Data, Dict, EpisodeObject, Ex, Hash, HTTP, Log, MovieObject, Prefs, String  # @UnresolvedImport # pylint: disable=F0401
except ImportError:
    # Skip dummy import
    pass

try:
    import L, XML, Callback, Data, Redirect, Datetime, WebVideoURL, PopupDirectoryObject, CACHE_1HOUR, InputDirectoryItem, InputDirectoryObject, PrefsItem, Dict, MessageContainer, Function, DirectoryObject, MediaContainer, VideoItem, DirectoryItem, EpisodeObject, Ex, Hash, HTML, HTTP, handler, JSON, Log, MovieObject, NextPageObject, ObjectContainer, parallelize, Plugin, Prefs, PrefsObject, Regex, Resource, route, SeasonObject, SearchDirectoryObject, String, task, TVShowObject, VideoClipObject  # @UnresolvedImport # pylint: disable=F0401
except ImportError:
    # Skip dummy import
    pass

def login():
    Log.Info("Logging in to Hulu.")
    action = "authenticate"
    try:
        parameters = {'login': Prefs["email"], 'password': Prefs['password'], 'nonce': get_nonce()}
    except KeyError:
        Log.Warn("Hulu username or password not set!")
        return False

    data = post_API(action, parameters, True)
    if not data:
        Log.Debug("Login failure")
        return False
    else:
        Data.Save(LOGIN_QUEUE_TOKEN_NAME, data)
        Log.Debug("Hulu login successful.")
        return True


####################################################################################################
def generate_signature(action, parameters):
    SECRET_STRING = "mTGPli7doNEpGfaVB9fquWfuAis"
    sorted_parameters = sorted(parameters.iteritems(), key=operator.itemgetter(0))
    paramsString = ''
    for item1, item2 in sorted_parameters:
        paramsString += str(item1) + str(item2)
    data = SECRET_STRING + action + paramsString
    return Hash.SHA1(data)

####################################################################################################
def post_API(action , parameters, secure):
    if secure == True:
        url = 'https://secure.'
    elif secure == False:
        url = 'http://www.'

    url += 'hulu.com/api/1.0/' + action
    parameters['app'] = 'f8aa99ec5c28937cf3177087d149a96b5a5efeeb'
    parameters['sig'] = generate_signature(action, parameters)
    headers = {'Referer':'http://download.hulu.com/huludesktop.swf?ver=0.1.0'}
    Log.Debug("Sending HTTP POST to {url}, Headers: {headers}, Body: {body}".format(url=url, headers=headers, body=urllib.urlencode(parameters)))
    try:
        response = HTTP.Request(url, headers=headers, values=parameters).content
        Log.Debug("Got response " + str(response))
        return response

    except Ex.HTTPError:
        Log.Exception("Failed to perform action " + action)

def update_login_token():
    xml_string = Data.Load(LOGIN_QUEUE_TOKEN_NAME)
    tree = XML.ElementFromString(xml_string)
    Dict['expiration'] = tree.findtext('token-expires-at')
    Dict['usertoken'] = tree.findtext('token')
    Dict['planid'] = tree.findtext('plid')
    Dict['userid'] = tree.findtext('id')

####################################################################################################

def check_login_token():
    if Data.Exists(LOGIN_QUEUE_TOKEN_NAME):
        update_login_token()
        expires = time.strptime(Dict['expiration'], "%Y-%m-%dT%H:%M:%SZ")
        now = time.localtime()
        if now > expires:
            Log.Info('Login token expired.')
            return login()
        else:
            return True
    else:
        return login()

def get_nonce():
    action = 'nonce'
    values = {}
    data = post_API(action, values, True)
    nonce = re.compile('<nonce>(.+?)</nonce>').findall(data)[0]
    Log.Debug("Got nonce " + str(nonce))
    return nonce

def get_feed(url, post_data=None):
    try:
        headers = {'Referer':'http://download.hulu.com/hulu10.html'}
        if not post_data:
            action = "GET"
            Log.Debug("Sending HTTP GET to '{}', Headers: {}".format(url, headers))
            response = HTTP.Request(url, headers=headers).content
        else:
            action = "POST"
            Log.Debug("Sending HTTP POST to '{}', Headers: {}, Body: '{}'".format(url, headers, post_data))
            response = HTTP.Request(url, headers=headers, data=post_data).content
    except Ex.HTTPError:
        Log.Exception("Failed to perform action {} on URL: '{}'".format(action, url))
    Log.Debug("Got response '%s'", response)
    return response


def get_shows(limit=50, sort_up=True):
    if sort_up:
        order_by = "name%20asc"
    else:
        order_by = "name%20desc"
    page = 1
    total = 50
    URL = BASE_URL + "shows?dp_id=hulu&limit={limit}&page={page}&order_by={order}&total={total}"
    URL = URL.format(limit=limit, page=page, order=order_by, total=total)
    Log.Debug("Getting shows from URL '{}'.".format(URL))    
    shows_xml = XML.ElementFromURL(URL)
    shows_list = Item_List.from_xml_node(shows_xml, Show).items
    shows_list = sorted(shows_list, key=lambda show: show.name)
    return shows_list


def get_videos_for_show(show_id, limit=50, sort_up=True):
    if sort_up:
        order_by = "name%20asc"
    else:
        order_by = "name%20desc"
    page = 1
    URL = BASE_URL + "videos?dp_id=hulu&limit={limit}&page={page}&order_by={order}&show_id={show_id}"
    URL = URL.format(limit=limit, page=page, order=order_by, show_id=show_id)
    Log.Debug("Getting videos from URL '{}'.".format(URL))
    videos_xml = XML.ElementFromURL(URL)
    video_list = Item_List.from_xml_node(videos_xml, Video).items
#     video_list = sorted(video_list, key=lambda video: video.eid)
    return video_list


def get_search_results(query, page_number):
    results_url = HULU_SEARCH_URL % (query, int(Prefs["items_per_page"]), page_number)
    Log.Debug("Getting results from '{}'.".format(results_url))
    results_xml = XML.ObjectFromURL(results_url)
    Log.Debug(XML.StringFromElement(results_xml))
    videos_node = get_xml_node(results_xml, "videos")
    videos_list = Item_List.from_xml_node(videos_node, Video)

    video_list = []
    for video in videos_list.items:
        video_thumbnail_url = video.get_thumbnail_url()
        video_url = video.get_embed_url()
        if video_url and video_thumbnail_url :
            video_list.add(EpisodeObject(
                rating_key=video_thumbnail_url,
                key=WebVideoURL(video_url),
                title=video.title,
                summary=video.description,
                thumb=Resource.ContentsOfURLWithFallback(video_thumbnail_url)))
    return video_list
