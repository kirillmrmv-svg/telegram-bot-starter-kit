import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from config import settings
from database import get_user, set_terms_accepted, set_user_language, upsert_user
from keyboard import (
    get_back_to_terms_keyboard,
    get_language_keyboard,
    get_main_menu_keyboard,
    get_terms_screen_keyboard,
)
from locales import t

logger = logging.getLogger(__name__)
router = Router()


def _build_start_screen_text() -> str:
    """Two-part start screen (EN + ES) with description above and language prompt below."""
    top_en = t("bot_description", "en")
    top_es = t("bot_description", "es")
    bottom_en = t("choose_language", "en")
    bottom_es = t("choose_language", "es")

    return (
        f"{top_en}\n\n"
        f"{top_es}"
        "\n\n\n"
        "────────────────────\n\n"
        f"{bottom_en}\n"
        f"{bottom_es}"
    )


async def _get_user_lang(user_id: int) -> str:
    user = await get_user(user_id)
    if isinstance(user, dict) and user.get("lang"):
        return str(user["lang"])
    return settings.DEFAULT_LANG


async def _send_terms_screen(target: Message | CallbackQuery, lang: str) -> None:
    text = t("terms_and_privacy_prompt", lang)
    markup = get_terms_screen_keyboard(lang)

    if isinstance(target, CallbackQuery) and target.message:
        try:
            await target.message.edit_text(text, reply_markup=markup)
            return
        except Exception:
            await target.message.answer(text, reply_markup=markup)
            return

    if isinstance(target, Message):
        await target.answer(text, reply_markup=markup)


async def _send_main_menu(target: Message | CallbackQuery, lang: str) -> None:
    text = t("main_menu_title", lang)
    markup = get_main_menu_keyboard(lang)

    if isinstance(target, CallbackQuery) and target.message:
        try:
            await target.message.edit_text(text, reply_markup=markup)
            return
        except Exception:
            await target.message.answer(text, reply_markup=markup)
            return

    if isinstance(target, Message):
        await target.answer(text, reply_markup=markup)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    if not message.from_user:
        return

    await upsert_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        default_lang=settings.DEFAULT_LANG,
    )

    await message.answer(
        _build_start_screen_text(),
        reply_markup=get_language_keyboard(),
    )


@router.callback_query(F.data.startswith("lang:"))
async def cb_select_language(callback: CallbackQuery) -> None:
    if not callback.from_user or not callback.data:
        return

    lang = callback.data.split(":", maxsplit=1)[1].strip().lower()
    if lang not in {"en", "es"}:
        lang = settings.DEFAULT_LANG

    await set_user_language(
        user_id=callback.from_user.id,
        lang=lang,
        username=callback.from_user.username,
    )

    await callback.answer(t("lang_saved", lang))

    user = await get_user(callback.from_user.id)
    accepted_terms = bool(user.get("accepted_terms")) if isinstance(user, dict) else False

    if accepted_terms:
        await _send_main_menu(callback, lang)
    else:
        await _send_terms_screen(callback, lang)


@router.callback_query(F.data == "accept_terms")
async def cb_accept_terms(callback: CallbackQuery) -> None:
    if not callback.from_user:
        return

    lang = await _get_user_lang(callback.from_user.id)
    await set_terms_accepted(user_id=callback.from_user.id, accepted=True)
    await callback.answer(t("terms_accepted", lang))
    await _send_main_menu(callback, lang)


@router.callback_query(F.data == "menu:help")
async def cb_menu_help(callback: CallbackQuery) -> None:
    if not callback.from_user:
        return

    lang = await _get_user_lang(callback.from_user.id)
    await callback.answer()
    if callback.message:
        await callback.message.edit_text(
            t("help_text", lang),
            reply_markup=get_main_menu_keyboard(lang),
        )


@router.callback_query(F.data == "menu:language")
async def cb_menu_language(callback: CallbackQuery) -> None:
    if not callback.from_user:
        return

    await callback.answer()
    if callback.message:
        await callback.message.edit_text(
            _build_start_screen_text(),
            reply_markup=get_language_keyboard(),
        )


async def _send_legal_document(
    callback: CallbackQuery,
    lang: str,
    text_key: str,
) -> None:
    await callback.answer()
    if not callback.message:
        return

    text = t(text_key, lang)
    markup = get_back_to_terms_keyboard(lang)
    try:
        await callback.message.edit_text(text, reply_markup=markup)
    except Exception:
        await callback.message.answer(text, reply_markup=markup)


@router.callback_query(F.data == "terms:agreement")
async def cb_terms_agreement(callback: CallbackQuery) -> None:
    if not callback.from_user:
        return
    lang = await _get_user_lang(callback.from_user.id)
    await _send_legal_document(callback, lang, "user_agreement_text")


@router.callback_query(F.data == "terms:privacy")
async def cb_terms_privacy(callback: CallbackQuery) -> None:
    if not callback.from_user:
        return
    lang = await _get_user_lang(callback.from_user.id)
    await _send_legal_document(callback, lang, "privacy_policy_text")


@router.callback_query(F.data == "terms:back")
async def cb_terms_back(callback: CallbackQuery) -> None:
    if not callback.from_user:
        return
    lang = await _get_user_lang(callback.from_user.id)
    await callback.answer()
    await _send_terms_screen(callback, lang)


@router.callback_query(F.data == "terms:back_to_lang")
async def cb_terms_back_to_lang(callback: CallbackQuery) -> None:
    if not callback.from_user:
        return
    await callback.answer()
    if callback.message:
        try:
            await callback.message.edit_text(
                _build_start_screen_text(),
                reply_markup=get_language_keyboard(),
            )
        except Exception:
            await callback.message.answer(
                _build_start_screen_text(),
                reply_markup=get_language_keyboard(),
            )