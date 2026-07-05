import time

START_TIME = time.time()

TOTAL_REQUESTS = 0

CACHE_HITS = 0

CACHE_MISSES = 0

TOTAL_RESPONSE_TIME = 0.0


def record_request(response_time: float, cached: bool):

    global TOTAL_REQUESTS
    global CACHE_HITS
    global CACHE_MISSES
    global TOTAL_RESPONSE_TIME

    TOTAL_REQUESTS += 1

    TOTAL_RESPONSE_TIME += response_time

    if cached:
        CACHE_HITS += 1
    else:
        CACHE_MISSES += 1


def get_metrics():

    uptime = round(time.time() - START_TIME, 2)

    avg = 0

    if TOTAL_REQUESTS:

        avg = round(
            TOTAL_RESPONSE_TIME / TOTAL_REQUESTS,
            2
        )

    hit_rate = 0

    if TOTAL_REQUESTS:

        hit_rate = round(
            (CACHE_HITS / TOTAL_REQUESTS) * 100,
            2
        )

    return {

        "uptime_seconds": uptime,

        "total_requests": TOTAL_REQUESTS,

        "cache_hits": CACHE_HITS,

        "cache_misses": CACHE_MISSES,

        "cache_hit_rate": hit_rate,

        "average_response_ms": avg

    }