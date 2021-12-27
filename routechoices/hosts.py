from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host('www', 'routechoices.urls', name='www'),
    host('api', 'routechoices.api.urls', name='api'),
    host(
        '(?P<club_slug>[a-zA-Z0-9][a-zA-Z0-9-]+)', 
        'routechoices.club.urls',
        callback='routechoices.club.urls.set_club',
        name='clubs'),
)
