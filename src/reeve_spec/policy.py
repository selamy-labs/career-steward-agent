from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


SECRET_LIKE = re.compile(
    r"(access[_-]?token|refresh[_-]?token|api[_-]?key|api[_-]?hash|client[_-]?secret|private[_-]?key|password)",
    re.IGNORECASE,
)
PRIVATE_PATH = re.compile(r"(/Users/|/home/|/opt/data/(?!wiki|work)|/root/)")
EMAIL = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
PHONE = re.compile(r"(?:\+?\d[\d(). -]{7,}\d)")


@dataclass(frozen=True)
class ApprovalRequest:
    channel: str
    recipient: str
    exact_text: str
    approval_text: str
    turn_id: str


def exact_text_approved(request: ApprovalRequest) -> bool:
    required = [request.channel, request.recipient, request.exact_text]
    approval = request.approval_text
    return all(part and part in approval for part in required)


def validate_external_action(action: dict[str, Any], policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    name = action.get("action")
    forbidden = set(policy.get("sideEffects", {}).get("forbidden", []))
    exact = set(policy.get("sideEffects", {}).get("requireExactApproval", []))
    if name in forbidden:
        errors.append(f"forbidden action requested: {name}")
    if name in exact:
        approval = action.get("approval") or {}
        req = ApprovalRequest(
            channel=str(action.get("channel", "")),
            recipient=str(action.get("recipient", "")),
            exact_text=str(action.get("text", "")),
            approval_text=str(approval.get("text", "")),
            turn_id=str(approval.get("turn_id", "")),
        )
        if not exact_text_approved(req):
            errors.append(f"missing exact-text approval for {name}")
        if approval.get("expired", False):
            errors.append(f"approval expired for {name}")
    return errors


def privacy_errors(text: str) -> list[str]:
    errors: list[str] = []
    if SECRET_LIKE.search(text):
        errors.append("secret-like token name/value detected")
    if PRIVATE_PATH.search(text):
        errors.append("private/local path detected")
    if EMAIL.search(text):
        errors.append("email address detected")
    if PHONE.search(text):
        errors.append("phone number detected")
    return errors


def public_safe(text: str) -> bool:
    return not privacy_errors(text)

