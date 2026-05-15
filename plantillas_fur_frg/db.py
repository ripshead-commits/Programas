"""
Capa de persistencia con SQLite. Una sola tabla `submissions` con los datos
serializados como JSON en una columna TEXT.

El archivo .db se guarda junto al ejecutable (al lado del .exe) cuando se
empaqueta con PyInstaller, o en el directorio del script en modo desarrollo.
"""
import json
import os
import sqlite3
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any


def _app_dir() -> Path:
    """Carpeta donde reside el .exe o el script en desarrollo."""
    if getattr(sys, "frozen", False):  # PyInstaller
        return Path(sys.executable).parent
    return Path(__file__).parent


DB_PATH = _app_dir() / "plantillas_fur_frg.db"


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS submissions (
                id TEXT PRIMARY KEY,
                module_id TEXT NOT NULL,
                label TEXT,
                data TEXT NOT NULL,
                downloaded INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_subs_module_created "
            "ON submissions(module_id, created_at DESC)"
        )


def create_submission(module_id: str, data: dict, label: str | None = None,
                      downloaded: bool = False) -> dict:
    now = datetime.now().isoformat(timespec="seconds")
    doc = {
        "id": str(uuid.uuid4()),
        "module_id": module_id.lower(),
        "label": label,
        "data": data,
        "downloaded": bool(downloaded),
        "created_at": now,
        "updated_at": now,
    }
    with _connect() as conn:
        conn.execute(
            "INSERT INTO submissions (id, module_id, label, data, downloaded, created_at, updated_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                doc["id"],
                doc["module_id"],
                doc["label"],
                json.dumps(data, ensure_ascii=False),
                1 if downloaded else 0,
                doc["created_at"],
                doc["updated_at"],
            ),
        )
    return doc


def list_submissions(module_id: str | None = None, limit: int = 200) -> list[dict]:
    with _connect() as conn:
        if module_id:
            rows = conn.execute(
                "SELECT * FROM submissions WHERE module_id = ? "
                "ORDER BY created_at DESC LIMIT ?",
                (module_id.lower(), limit),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM submissions ORDER BY created_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
    return [_row_to_dict(r) for r in rows]


def get_submission(submission_id: str) -> dict | None:
    with _connect() as conn:
        row = conn.execute(
            "SELECT * FROM submissions WHERE id = ?", (submission_id,)
        ).fetchone()
    return _row_to_dict(row) if row else None


def delete_submission(submission_id: str) -> bool:
    with _connect() as conn:
        cur = conn.execute("DELETE FROM submissions WHERE id = ?", (submission_id,))
        return cur.rowcount > 0


def _row_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "id": row["id"],
        "module_id": row["module_id"],
        "label": row["label"],
        "data": json.loads(row["data"]),
        "downloaded": bool(row["downloaded"]),
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }
