# === Stage 9: Постраничный вывод ===
# Project: CakeDesigner
from typing import Iterable, List, Tuple


def page_from_collection(collection: Iterable, page: int, per_page: int) -> List:
    items = list(collection)
    if per_page <= 0:
        per_page = 1
    total_pages = max(1, (len(items) + per_page - 1) // per_page)
    page = max(1, min(page, total_pages))
    start = (page - 1) * per_page
    return items[start:start + per_page]


def total_pages_from_collection(collection: Iterable, per_page: int) -> int:
    if per_page <= 0:
        per_page = 1
    return max(1, (len(list(collection)) + per_page - 1) // per_page)


def page_metadata(collection: Iterable, page: int, per_page: int) -> dict:
    items = list(collection)
    total = len(items)
    total_pages = max(1, (total + per_page - 1) // per_page)
    page = max(1, min(page, total_pages))
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "start": start,
        "end": end,
    }


def page_and_meta(collection: Iterable, page: int, per_page: int) -> Tuple[List, dict]:
    return page_from_collection(collection, page, per_page), page_metadata(collection, page, per_page)


def paginate(cakes: Iterable, page: int, per_page: int) -> Tuple[List, dict]:
    return page_and_meta(cakes, page, per_page)


def render_pagination_html(meta: dict) -> str:
    total_pages = meta["total_pages"]
    page = meta["page"]
    prev = max(1, page - 1)
    next = min(total_pages, page + 1)
    buttons = [
        f'<button class="pg" data-page="{prev}" disabled>' if page == 1 else f'<button class="pg" data-page="{prev}">&laquo;</button>',
        f'<span class="pg-current">{page}</span>',
        f'<button class="pg" data-page="{next}">&raquo;</button>' if page == total_pages else f'<button class="pg" data-page="{next}">&raquo;</button>',
    ]
    return ''.join(buttons)


def parse_page_request(query: dict) -> Tuple[int, int]:
    page = int(query.get("page", 1))
    per_page = int(query.get("per_page", 10))
    return page, per_page


def apply_pagination(items: List, query: dict) -> Tuple[List, dict]:
    page, per_page = parse_page_request(query)
    return paginate(items, page, per_page), page_metadata(items, page, per_page)
