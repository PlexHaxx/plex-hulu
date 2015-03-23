from XML_Utils import get_xml_text_value

try:
    import Log  # @UnresolvedImport # pylint: disable=F0401
except ImportError:
    pass

class Item_List(object):
    def __init__(self, items):
        self.items = items
        self.count = len(items)

    @classmethod
    def from_xml_node(cls, xml_node, item_type):
        items = []
        for item_node in xml_node.iter(item_type.TAG):
            items.append(item_type.from_xml_node(item_node))
        return cls(items)

class Video(object):
    TAG = "video"
    EMBED_PREFIX = "https://secure.hulu.com/embed/"
    def __init__(self, available_at, categories, collation_title, company_canonical_name, company_id, company_name, composite_available_at, composite_expires_at, content_id, content_rating, content_rating_reason, video_copyright, cp_id, cp_identifier, description, duration, eid, embed_permitted, episode_number, expires_at, has_captions, has_hd, has_plus_living_room, has_plus_mobile, has_plus_preview, has_plus_web, video_num_id, include_company_logo, is_plus_web_only, language, media_type, original_premiere_date, package_id, parent_channel_id, parent_channel_name, pid, plus_living_room_available_at, plus_living_room_expires_at, plus_mobile_available_at, plus_mobile_expires_at, plus_only, plus_web_available_at, plus_web_expires_at, positive_votes_count, programming_type, promotional_link, promotional_text, rating, reviews_count, season_number, show_canonical_name, show_id, show_name, studio, thumbnail_url_16x9_large, thumbnail_url_16x9_medium, thumbnail_url_4x3_medium, title, tune_in_information, video_id, video_type, votes_count, thumbnail_url):
        self.available_at = available_at
        self.categories = categories
        self.collation_title = collation_title
        self.company_canonical_name = company_canonical_name
        self.company_id = company_id
        self.company_name = company_name
        self.composite_available_at = composite_available_at
        self.composite_expires_at = composite_expires_at
        self.content_id = content_id
        self.content_rating = content_rating
        self.content_rating_reason = content_rating_reason
        self.copyright = video_copyright
        self.cp_id = cp_id
        self.cp_identifier = cp_identifier
        self.description = description
        self.duration = duration
        self.eid = eid
        self.embed_permitted = embed_permitted
        self.episode_number = episode_number
        self.expires_at = expires_at
        self.has_captions = has_captions
        self.has_hd = has_hd
        self.has_plus_living_room = has_plus_living_room
        self.has_plus_mobile = has_plus_mobile
        self.has_plus_preview = has_plus_preview
        self.has_plus_web = has_plus_web
        self.video_num_id = video_num_id
        self.include_company_logo = include_company_logo
        self.is_plus_web_only = is_plus_web_only
        self.language = language
        self.media_type = media_type
        self.original_premiere_date = original_premiere_date
        self.package_id = package_id
        self.parent_channel_id = parent_channel_id
        self.parent_channel_name = parent_channel_name
        self.pid = pid
        self.plus_living_room_available_at = plus_living_room_available_at
        self.plus_living_room_expires_at = plus_living_room_expires_at
        self.plus_mobile_available_at = plus_mobile_available_at
        self.plus_mobile_expires_at = plus_mobile_expires_at
        self.plus_only = plus_only
        self.plus_web_available_at = plus_web_available_at
        self.plus_web_expires_at = plus_web_expires_at
        self.positive_votes_count = positive_votes_count
        self.programming_type = programming_type
        self.promotional_link = promotional_link
        self.promotional_text = promotional_text
        self.rating = rating
        self.reviews_count = reviews_count
        self.season_number = season_number
        self.show_canonical_name = show_canonical_name
        self.show_id = show_id
        self.show_name = show_name
        self.studio = studio
        self.thumbnail_url_16x9_large = thumbnail_url_16x9_large
        self.thumbnail_url_16x9_medium = thumbnail_url_16x9_medium
        self.thumbnail_url_4x3_medium = thumbnail_url_4x3_medium
        self.title = title
        self.tune_in_information = tune_in_information
        self.video_type = video_type
        self.votes_count = votes_count
        self.thumbnail_url = thumbnail_url
        self.id = video_id

    @classmethod
    def from_xml_node(cls, xml_node):
        available_at = get_xml_text_value(xml_node, "available_at")
        categories = get_xml_text_value(xml_node, "categories")
        collation_title = get_xml_text_value(xml_node, "collation_title")
        company_canonical_name = get_xml_text_value(xml_node, "company_canonical_name")
        company_id = get_xml_text_value(xml_node, "company_id")
        company_name = get_xml_text_value(xml_node, "company_name")
        composite_available_at = get_xml_text_value(xml_node, "composite_available_at")
        composite_expires_at = get_xml_text_value(xml_node, "composite_expires_at")
        content_id = get_xml_text_value(xml_node, "content_id")
        content_rating = get_xml_text_value(xml_node, "content_rating")
        content_rating_reason = get_xml_text_value(xml_node, "content_rating_reason")
        video_copyright = get_xml_text_value(xml_node, "copyright")
        cp_id = get_xml_text_value(xml_node, "cp_id")
        cp_identifier = get_xml_text_value(xml_node, "cp_identifier")
        description = get_xml_text_value(xml_node, "description")
        duration = get_xml_text_value(xml_node, "duration")
        eid = get_xml_text_value(xml_node, "eid")
        embed_permitted = get_xml_text_value(xml_node, "embed_permitted")
        episode_number = get_xml_text_value(xml_node, "episode_number")
        expires_at = get_xml_text_value(xml_node, "expires_at")
        has_captions = get_xml_text_value(xml_node, "has_captions")
        has_hd = get_xml_text_value(xml_node, "has_hd")
        has_plus_living_room = get_xml_text_value(xml_node, "has_plus_living_room")
        has_plus_mobile = get_xml_text_value(xml_node, "has_plus_mobile")
        has_plus_preview = get_xml_text_value(xml_node, "has_plus_preview")
        has_plus_web = get_xml_text_value(xml_node, "has_plus_web")
        video_num_id = get_xml_text_value(xml_node, "video_num_id")
        include_company_logo = get_xml_text_value(xml_node, "include_company_logo")
        is_plus_web_only = get_xml_text_value(xml_node, "is_plus_web_only")
        language = get_xml_text_value(xml_node, "language")
        media_type = get_xml_text_value(xml_node, "media_type")
        original_premiere_date = get_xml_text_value(xml_node, "original_premiere_date")
        package_id = get_xml_text_value(xml_node, "package_id")
        parent_channel_id = get_xml_text_value(xml_node, "parent_channel_id")
        parent_channel_name = get_xml_text_value(xml_node, "parent_channel_name")
        pid = get_xml_text_value(xml_node, "pid")
        plus_living_room_available_at = get_xml_text_value(xml_node, "plus_living_room_available_at")
        plus_living_room_expires_at = get_xml_text_value(xml_node, "plus_living_room_expires_at")
        plus_mobile_available_at = get_xml_text_value(xml_node, "plus_mobile_available_at")
        plus_mobile_expires_at = get_xml_text_value(xml_node, "plus_mobile_expires_at")
        plus_only = get_xml_text_value(xml_node, "plus_only")
        plus_web_available_at = get_xml_text_value(xml_node, "plus_web_available_at")
        plus_web_expires_at = get_xml_text_value(xml_node, "plus_web_expires_at")
        positive_votes_count = get_xml_text_value(xml_node, "positive_votes_count")
        programming_type = get_xml_text_value(xml_node, "programming_type")
        promotional_link = get_xml_text_value(xml_node, "promotional_link")
        promotional_text = get_xml_text_value(xml_node, "promotional_text")
        rating = get_xml_text_value(xml_node, "rating")
        reviews_count = get_xml_text_value(xml_node, "reviews_count")
        season_number = get_xml_text_value(xml_node, "season_number")
        show_canonical_name = get_xml_text_value(xml_node, "show_canonical_name")
        show_id = get_xml_text_value(xml_node, "show_id")
        show_name = get_xml_text_value(xml_node, "show_name")
        studio = get_xml_text_value(xml_node, "studio")
        thumbnail_url = get_xml_text_value(xml_node, "thumbnail-url")
        thumbnail_url_16x9_large = get_xml_text_value(xml_node, "thumbnail_url_16x9_large")
        thumbnail_url_16x9_medium = get_xml_text_value(xml_node, "thumbnail_url_16x9_medium")
        thumbnail_url_4x3_medium = get_xml_text_value(xml_node, "thumbnail_url_4x3_medium")
        title = get_xml_text_value(xml_node, "title")
        tune_in_information = get_xml_text_value(xml_node, "tune_in_information")
        video_type = get_xml_text_value(xml_node, "video_type")
        votes_count = get_xml_text_value(xml_node, "votes_count")
        video_id = get_xml_text_value(xml_node, "id")
        return cls(available_at, categories, collation_title, company_canonical_name, company_id, company_name, composite_available_at, composite_expires_at, content_id, content_rating, content_rating_reason, video_copyright, cp_id, cp_identifier, description, duration, eid, embed_permitted, episode_number, expires_at, has_captions, has_hd, has_plus_living_room, has_plus_mobile, has_plus_preview, has_plus_web, video_num_id, include_company_logo, is_plus_web_only, language, media_type, original_premiere_date, package_id, parent_channel_id, parent_channel_name, pid, plus_living_room_available_at, plus_living_room_expires_at, plus_mobile_available_at, plus_mobile_expires_at, plus_only, plus_web_available_at, plus_web_expires_at, positive_votes_count, programming_type, promotional_link, promotional_text, rating, reviews_count, season_number, show_canonical_name, show_id, show_name, studio, thumbnail_url_16x9_large, thumbnail_url_16x9_medium, thumbnail_url_4x3_medium, title, tune_in_information, video_id, video_type, votes_count, thumbnail_url)

    def get_embed_url(self):
        try:
            Log.Debug("Returning embed URL for for video with ID '%s'.", self.video_num_id)
            return Video.EMBED_PREFIX + self.eid
        except TypeError:
            Log.Error("EID is not set for video with ID '{}'.", self.video_num_id)
            return None

    def get_thumbnail_url(self):
        THUMBNAIL_VARS = (self.thumbnail_url, self.thumbnail_url_16x9_large, self.thumbnail_url_16x9_medium, self.thumbnail_url_4x3_medium)
        for thumb_var in THUMBNAIL_VARS:
            if thumb_var:
                return thumb_var
        return None

class Show(object):
    TAG = "show"
    def __init__(self, availability_notes, canonical_name, clips_count, collation_name, company_canonical_name, company_id, company_name, content_age_group, description, device_id, dp_identifier, episode_clips_count, feature_film_content_id, feature_film_id, feature_films_count, film_clips_count, full_episodes_count, genre, has_hd, has_plus_living_room, has_plus_mobile, show_num_id, include_company_logo, max_season_number, min_season_number, name, original_premiere_date, package_group_id, package_group_id, plus_web_videos_count, primary_channel_id, primary_channel_name, primary_channel_name, rating, sa_instance_state, show_id, total_seasons_count, videos_count):
        self.availability_notes = availability_notes
        self.canonical_name = canonical_name
        self.clips_count = clips_count
        self.collation_name = collation_name
        self.company_canonical_name = company_canonical_name
        self.company_id = company_id
        self.company_name = company_name
        self.content_age_group = content_age_group
        self.description = description
        self.device_id = device_id
        self.dp_identifier = dp_identifier
        self.episode_clips_count = episode_clips_count
        self.feature_film_content_id = feature_film_content_id
        self.feature_film_id = feature_film_id
        self.feature_films_count = feature_films_count
        self.film_clips_count = film_clips_count
        self.full_episodes_count = full_episodes_count
        self.genre = genre
        self.has_hd = has_hd
        self.has_plus_living_room = has_plus_living_room
        self.has_plus_mobile = has_plus_mobile
        self.id = show_num_id
        self.include_company_logo = include_company_logo
        self.max_season_number = max_season_number
        self.min_season_number = min_season_number
        self.name = name
        self.original_premiere_date = original_premiere_date
        self.package_group_id = package_group_id
        self.package_group_id = package_group_id
        self.plus_web_videos_count = plus_web_videos_count
        self.primary_channel_id = primary_channel_id
        self.primary_channel_name = primary_channel_name
        self.primary_channel_name = primary_channel_name
        self.rating = rating
        self.sa_instance_state = sa_instance_state
        self.show_id = show_id
        self.total_seasons_count = total_seasons_count
        self.videos_count = videos_count
        super(Show, self).__init__()


    def get_thumbnail_url(self):
        if self.show_id:
            return "http://ib1.huluim.com/show/{}?size=220x124&region=us".format(self.show_id)
        else:
            return None


    @classmethod
    def from_xml_node(cls, xml_node):
        availability_notes = get_xml_text_value(xml_node, "availability_notes")
        canonical_name = get_xml_text_value(xml_node, "canonical_name")
        clips_count = get_xml_text_value(xml_node, "clips_count")
        collation_name = get_xml_text_value(xml_node, "collation_name")
        company_canonical_name = get_xml_text_value(xml_node, "company_canonical_name")
        company_id = get_xml_text_value(xml_node, "company_id")
        company_name = get_xml_text_value(xml_node, "company_name")
        content_age_group = get_xml_text_value(xml_node, "content_age_group")
        description = get_xml_text_value(xml_node, "description")
        device_id = get_xml_text_value(xml_node, "device_id")
        dp_identifier = get_xml_text_value(xml_node, "dp_identifier")
        episode_clips_count = get_xml_text_value(xml_node, "episode_clips_count")
        feature_film_content_id = get_xml_text_value(xml_node, "feature_film_content_id")
        feature_film_id = get_xml_text_value(xml_node, "feature_film_id")
        feature_films_count = get_xml_text_value(xml_node, "feature_films_count")
        film_clips_count = get_xml_text_value(xml_node, "film_clips_count")
        full_episodes_count = get_xml_text_value(xml_node, "full_episodes_count")
        genre = get_xml_text_value(xml_node, "genre")
        has_hd = get_xml_text_value(xml_node, "has_hd")
        has_plus_living_room = get_xml_text_value(xml_node, "has_plus_living_room")
        has_plus_mobile = get_xml_text_value(xml_node, "has_plus_mobile")
        show_num_id = get_xml_text_value(xml_node, "id")
        include_company_logo = get_xml_text_value(xml_node, "include_company_logo")
        max_season_number = get_xml_text_value(xml_node, "max_season_number")
        min_season_number = get_xml_text_value(xml_node, "min_season_number")
        name = get_xml_text_value(xml_node, "name")
        original_premiere_date = get_xml_text_value(xml_node, "original_premiere_date")
        package_group_id = get_xml_text_value(xml_node, "package_group_id")
        plus_web_videos_count = get_xml_text_value(xml_node, "plus_web_videos_count")
        primary_channel_id = get_xml_text_value(xml_node, "primary_channel_id")
        primary_channel_name = get_xml_text_value(xml_node, "primary_channel_name")
        rating = get_xml_text_value(xml_node, "rating")
        sa_instance_state = get_xml_text_value(xml_node, "sa_instance_state")
        show_id = get_xml_text_value(xml_node, "show_id")
        total_seasons_count = get_xml_text_value(xml_node, "total_seasons_count")
        videos_count = get_xml_text_value(xml_node, "videos_count")
        return cls(availability_notes, canonical_name, clips_count, collation_name, company_canonical_name, company_id, company_name, content_age_group, description, device_id, dp_identifier, episode_clips_count, feature_film_content_id, feature_film_id, feature_films_count, film_clips_count, full_episodes_count, genre, has_hd, has_plus_living_room, has_plus_mobile, show_num_id, include_company_logo, max_season_number, min_season_number, name, original_premiere_date, package_group_id, package_group_id, plus_web_videos_count, primary_channel_id, primary_channel_name, primary_channel_name, rating, sa_instance_state, show_id, total_seasons_count, videos_count)
